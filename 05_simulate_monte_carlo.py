import pandas as pd
import numpy as np
from itertools import product
from tqdm import tqdm
from fmap_helpers import (
    calculate_mtmltv,
    get_transition_probabilities,
    calculate_credit_loss,
    LoanState
)

# Set a random seed for reproducibility
np.random.seed(42)

# --- CONFIGURATION ---
N_SIMULATION_PATHS = 10000 # Number of paths to simulate for each loan/scenario

# Load data
loans_df = pd.read_csv('loans.csv')
scenarios_df = pd.read_csv('scenarios.csv')

results = []

# --- VALIDATION FIX: Increase simulation paths and average results ---
# The loop now includes the number of simulation paths
for (loan_idx, loan), scenario_id, path_num in tqdm(
    product(
        loans_df.iterrows(),
        scenarios_df['scenario_id'].unique(),
        range(N_SIMULATION_PATHS)
    ),
    total=len(loans_df) * len(scenarios_df['scenario_id'].unique()) * N_SIMULATION_PATHS,
    desc="Running Monte Carlo Paths"
):
    scenario_data = scenarios_df[scenarios_df['scenario_id'] == scenario_id]
    
    # Initialize loan state for the single simulation path
    current_loan_state = LoanState.PERFORMING
    loan_upb = loan['initial_upb']

    for month_idx, mev in scenario_data.iterrows():
        credit_loss = 0

        if current_loan_state not in [LoanState.DEFAULT, LoanState.PREPAY]:
            # 1. Calculate MTMLTV
            current_mtmltv = calculate_mtmltv(
                current_upb=loan_upb,
                original_property_value=loan['original_property_value'],
                current_hpi=mev['hpi_index'],
                base_hpi=loan['base_hpi']
            )

            # 2. Get transition probabilities for the current state
            transitions = get_transition_probabilities(loan, mev, current_mtmltv)
            current_transitions = transitions.get(current_loan_state, {})

            # Ensure probabilities sum to 1 for np.random.choice
            # This is a fallback, the new get_transition_matrix should handle this
            if sum(current_transitions.values()) > 0 and not np.isclose(sum(current_transitions.values()), 1.0):
                # Find the state to adjust (usually the current state)
                state_to_adjust = current_loan_state if current_loan_state in current_transitions else list(current_transitions.keys())[0]
                current_transitions[state_to_adjust] = max(0, 1.0 - sum(v for k, v in current_transitions.items() if k != state_to_adjust))


            # 3. Select a single, discrete next state
            possible_next_states = list(current_transitions.keys())
            state_probabilities = list(current_transitions.values())
            
            if not possible_next_states or sum(state_probabilities) == 0:
                # No defined transitions, stay in the same state
                next_state = current_loan_state
            else:
                # Normalize probabilities just in case of floating point inaccuracies
                state_probabilities = np.array(state_probabilities) / sum(state_probabilities)
                next_state = np.random.choice(possible_next_states, p=state_probabilities)

            # 4. If the new state is Default, calculate loss
            if next_state == LoanState.DEFAULT:
                credit_loss = calculate_credit_loss(loan, current_mtmltv)
            
            current_loan_state = next_state
            loan_upb *= 0.998 # Simplified amortization

        results.append({
            'loan_id': loan['loan_id'],
            'scenario_id': scenario_id,
            'path_num': path_num,
            'month': mev['month'],
            'final_state': current_loan_state.value,
            'credit_loss': credit_loss
        })

# Create DataFrame from all paths
full_results_df = pd.DataFrame(results)

# --- VALIDATION FIX: Aggregate results by taking the MEAN across all paths ---
agg_results_df = full_results_df.groupby(['loan_id', 'scenario_id', 'month']).agg(
    credit_loss=('credit_loss', 'mean'), # Changed from 'sum' to 'mean'
    final_state=('final_state', lambda x: x.value_counts().index[0]) # Most common final state
).reset_index()


# Save aggregated results
agg_results_df.to_csv('monte_carlo_results.csv', index=False)

print(f"Monte Carlo simulation complete ({N_SIMULATION_PATHS} paths). Averaged results saved to monte_carlo_results.csv")
