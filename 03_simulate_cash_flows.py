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

        # 2. Get transition probabilities and the full matrix
        probabilities = get_transition_probabilities(loan, mev, current_mtmltv)
        transition_matrix = get_transition_matrix(probabilities)

        # 3. Calculate the probability of entering the DEFAULT state *this month*
        # This is the probability of being in a non-terminal state times the probability of transitioning to default
        prob_entering_default = 0
        for state in LoanState:
            if state not in [LoanState.DEFAULT, LoanState.PREPAY]:
                prob_in_state = state_vector[STATE_TO_INDEX[state]]
                prob_trans_to_default = transition_matrix.loc[state, LoanState.DEFAULT]
                prob_entering_default += prob_in_state * prob_trans_to_default

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
            'credit_loss': credit_loss
        })

# Create DataFrame and save
results_df = pd.DataFrame(results)
results_df.to_csv('cashflow_results.csv', index=False)

print("Cash flow simulation complete. Results saved to cashflow_results.csv")
