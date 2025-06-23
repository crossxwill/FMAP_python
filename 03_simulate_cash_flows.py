import pandas as pd
import numpy as np
from itertools import product
from tqdm import tqdm
from fmap_helpers import (
    calculate_mtmltv,
    get_transition_probabilities,
    get_transition_matrix, # Import the matrix function
    calculate_credit_loss,
    LoanState,
    STATE_TO_INDEX,
    INDEX_TO_STATE
)

# Set a random seed for reproducibility, although this script is deterministic
np.random.seed(42)

# Load data
loans_df = pd.read_csv('loans.csv')
scenarios_df = pd.read_csv('scenarios.csv')

results = []

# Use tqdm for a progress bar
for (loan_idx, loan), scenario_id in tqdm(product(loans_df.iterrows(), scenarios_df['scenario_id'].unique()), total=len(loans_df) * len(scenarios_df['scenario_id'].unique())):
    scenario_data = scenarios_df[scenarios_df['scenario_id'] == scenario_id]
    
    loan_upb = loan['initial_upb']

    # --- VALIDATION FIX: Track state distribution over time ---
    # Initialize the state vector: 100% probability in PERFORMING state at month 0
    state_vector = np.zeros(len(LoanState))
    state_vector[STATE_TO_INDEX[LoanState.PERFORMING]] = 1.0

    for month_idx, mev in scenario_data.iterrows():
        # 1. Calculate MTMLTV
        current_mtmltv = calculate_mtmltv(
            current_upb=loan_upb,
            original_property_value=loan['original_property_value'],
            current_hpi=mev['hpi_index'],
            base_hpi=loan['base_hpi']
        )

        # 2. Get the full transition matrix for the current loan and scenario conditions
        # This matrix is now generated directly by a function that encapsulates all the
        # state transition logic from the white paper.
        probabilities = get_transition_probabilities(loan, mev, current_mtmltv)
        transition_matrix = get_transition_matrix(probabilities)

        # 3. Calculate the probability of entering the DEFAULT state *this month*
        # This is the probability of being in a non-terminal state times the probability of transitioning to default
        # It is the dot product of the current state distribution and the 'Default' column of the transition matrix.
        prob_entering_default = state_vector.dot(transition_matrix[LoanState.DEFAULT].values)

        # 4. Calculate expected credit loss for the month
        potential_loss = calculate_credit_loss(loan, current_mtmltv)
        credit_loss = potential_loss * prob_entering_default

        # 5. Update the state vector for the next month
        state_vector = state_vector.dot(transition_matrix.values)

        # Reduce UPB by a small amount to simulate amortization (simplified)
        loan_upb *= 0.998

        results.append({
            'loan_id': loan['loan_id'],
            'scenario_id': scenario_id,
            'month': mev['month'],
            'expected_credit_loss': credit_loss,
            # record full state distribution
            **{f'prob_{state.name}': state_vector[STATE_TO_INDEX[state]] for state in LoanState}
        })

# Create DataFrame and save
results_df = pd.DataFrame(results)
results_df.to_csv('cashflow_results.csv', index=False)

print("Cash flow simulation complete. Results saved to cashflow_results.csv")
