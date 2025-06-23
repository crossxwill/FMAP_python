import pandas as pd
import numpy as np
from itertools import product
from tqdm import tqdm
from fmap_helpers import (
    calculate_mtmltv,
    get_transition_probabilities, # Import the new function
    calculate_credit_loss,
    get_transition_matrix,
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
num_states = len(LoanState)

# Use tqdm for a progress bar
for (loan_idx, loan), scenario_id in tqdm(product(loans_df.iterrows(), scenarios_df['scenario_id'].unique()), total=len(loans_df) * len(scenarios_df['scenario_id'].unique())):
    scenario_data = scenarios_df[scenarios_df['scenario_id'] == scenario_id]

    # Initialize state vector: 100% probability in the PERFORMING state
    state_vector = np.zeros(num_states)
    state_vector[STATE_TO_INDEX[LoanState.PERFORMING]] = 1.0
    loan_upb = loan['initial_upb']

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

        # 3. Calculate probability of entering the default state this month
        # This is the dot product of the current state vector and the default column of the transition matrix.
        prob_entering_default = state_vector.dot(transition_matrix[LoanState.DEFAULT].values)

        # 4. Calculate potential credit loss
        potential_loss = calculate_credit_loss(loan, current_mtmltv)

        # 5. Calculate expected credit loss for the month
        expected_credit_loss = prob_entering_default * potential_loss

        # Store results for the current month
        month_results = {
            'loan_id': loan['loan_id'],
            'scenario_id': scenario_id,
            'month': mev['month'],
            'expected_credit_loss': expected_credit_loss
        }
        for state in LoanState:
            month_results[f'prob_{state.name}'] = state_vector[STATE_TO_INDEX[state]]
        results.append(month_results)

        # 6. Calculate next month's state vector
        state_vector = state_vector @ transition_matrix.values

        # Reduce UPB for next iteration
        loan_upb *= 0.998

# Create DataFrame and save
results_df = pd.DataFrame(results)
results_df.to_csv('markov_chain_results.csv', index=False)

print("Markov chain simulation complete. Results saved to markov_chain_results.csv")
