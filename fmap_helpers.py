import pandas as pd
import numpy as np
from enum import Enum

# Section 5.2: Loan State Definitions
class LoanState(Enum):
    PERFORMING = 'PER'
    MODIFIED_REPERFORMING = 'MRPL'
    NON_MODIFIED_REPERFORMING = 'NRPL'
    REPERFORMING = 'RPL'
    LIGHT_DELINQUENT = 'LDQ'
    SERIOUSLY_DELINQUENT = 'SDQ'
    DEEPLY_DELINQUENT = 'DDQ'
    PREPAY = 'Prepay'
    DEFAULT = 'Default'

# Mapping from state to an index for matrix operations
STATE_TO_INDEX = {state: i for i, state in enumerate(LoanState)}
INDEX_TO_STATE = {i: state for state, i in STATE_TO_INDEX.items()}


def calculate_mtmltv(current_upb, original_property_value, current_hpi, base_hpi):
    """
    Calculates the Mark-to-Market Loan-to-Value (MTMLTV) ratio.
    """
    if base_hpi == 0 or original_property_value == 0:
        return np.inf
    current_property_value = original_property_value * (current_hpi / base_hpi)
    if current_property_value == 0:
        return np.inf
    return current_upb / current_property_value

def get_transition_probabilities(loan, mev_scenario, current_mtmltv):
    """
    Placeholder for the behavioral models to calculate transition probabilities.
    NOTE: The actual equations and coefficients are not provided in the document.
    This function uses simplified logic for demonstration purposes.
    The probabilities are higher in a 'Recession' scenario.
    """
    # --- VALIDATION FIX: Make base default probability more sensitive to MTMLTV ---
    # The original formula had a floor of 0.01 for MTMLTV <= 1, leading to zero losses in Normal scenarios.
    # This new formula provides a smoother, more realistic probability curve.
    base_default_prob = 0.005 + (current_mtmltv * 0.015)
    base_prepay_prob = 0.02

    # --- Adjust base probabilities based on product type (as per Section 5.3) ---
    product_type = loan.get('product_type')
    if product_type == 'FRM 15/20yr':
        # Lower default risk for shorter-term loans, builds equity faster
        base_default_prob *= 0.8
    elif product_type == 'ARM':
        # Higher prepayment sensitivity for ARMs, especially in certain interest rate environments
        base_prepay_prob *= 1.5
    # FRM 30/40yr uses the baseline probabilities as a reference

    if mev_scenario['scenario_id'] == 'Recession':
        default_multiplier = 2.5
        prepay_multiplier = 0.5
    else: # Normal
        default_multiplier = 1.0
        prepay_multiplier = 1.0

    # Probabilities from Performing state
    prob_perf_to_ldq = base_default_prob * default_multiplier
    prob_perf_to_prepay = base_prepay_prob * prepay_multiplier
    prob_perf_to_ldq = min(prob_perf_to_ldq, 0.9) # Cap probability
    prob_perf_to_prepay = min(prob_perf_to_prepay, 0.9) # Cap probability
    prob_perf_to_perf = 1 - prob_perf_to_ldq - prob_perf_to_prepay

    # --- MTMLTV-driven default probabilities for delinquent states ---
    # The probability of default increases with delinquency severity and MTMLTV.
    prob_ldq_to_default = min(base_default_prob * 1.5 * default_multiplier, 0.9)
    prob_sdq_to_default = min(base_default_prob * 2.0 * default_multiplier, 0.9)
    prob_ddq_to_default = min(base_default_prob * 3.0 * default_multiplier, 0.9)

    # --- VALIDATION FIX: Ensure probabilities sum to 1 for delinquent states ---
    # Calculate reperforming probability as the remainder.
    prob_ldq_to_rpl = max(0, 1.0 - 0.4 - prob_ldq_to_default - (0.01 * prepay_multiplier))
    prob_sdq_to_rpl = max(0, 1.0 - 0.5 - prob_sdq_to_default - 0.0)
    prob_ddq_to_rpl = max(0, 1.0 - 0.6 - prob_ddq_to_default - 0.0)


    # Simplified transitions for other states
    # For a real model, each transition in Table 1 would have its own equation.
    probabilities = {
        LoanState.PERFORMING: {
            LoanState.PERFORMING: prob_perf_to_perf,
            LoanState.LIGHT_DELINQUENT: prob_perf_to_ldq,
            LoanState.PREPAY: prob_perf_to_prepay,
            LoanState.DEFAULT: 0.0
        },
        LoanState.LIGHT_DELINQUENT: {
            LoanState.SERIOUSLY_DELINQUENT: 0.4,
            LoanState.REPERFORMING: prob_ldq_to_rpl,
            LoanState.DEFAULT: prob_ldq_to_default,
            LoanState.PREPAY: 0.01 * prepay_multiplier
        },
        LoanState.SERIOUSLY_DELINQUENT: {
            LoanState.DEEPLY_DELINQUENT: 0.5,
            LoanState.REPERFORMING: prob_sdq_to_rpl,
            LoanState.DEFAULT: prob_sdq_to_default,
            LoanState.PREPAY: 0.0
        },
        LoanState.DEEPLY_DELINQUENT: {
            LoanState.DEEPLY_DELINQUENT: 0.6,
            LoanState.REPERFORMING: prob_ddq_to_rpl,
            LoanState.DEFAULT: prob_ddq_to_default,
            LoanState.PREPAY: 0.0
        },
        # Simplified for other states
        LoanState.REPERFORMING: {LoanState.PERFORMING: 0.9, LoanState.LIGHT_DELINQUENT: 0.1},
        LoanState.MODIFIED_REPERFORMING: {LoanState.PERFORMING: 0.9, LoanState.LIGHT_DELINQUENT: 0.1},
        LoanState.NON_MODIFIED_REPERFORMING: {LoanState.PERFORMING: 0.9, LoanState.LIGHT_DELINQUENT: 0.1},
    }

    return probabilities


def calculate_credit_loss(loan, current_mtmltv):
    """
    Placeholder for the loss severity model.
    NOTE: The actual equations are not provided in the document.
    This function uses a simplified Loss Given Default (LGD) based on MTMLTV.
    """
    # Simplified LGD: higher MTMLTV implies higher loss
    lgd = 0.1 + (current_mtmltv - 1) * 0.4 if current_mtmltv > 1 else 0.1
    lgd = min(lgd, 1.0) # Cap LGD at 100%
    
    # Loss = Exposure at Default (EAD) * LGD
    # EAD is assumed to be the current unpaid principal balance (UPB)
    credit_loss = loan['current_upb'] * lgd
    return credit_loss

def get_transition_matrix(probabilities):
    """
    Constructs the transition matrix for the Markov Chain simulation.
    """
    num_states = len(LoanState)
    matrix = pd.DataFrame(np.zeros((num_states, num_states)), index=list(LoanState), columns=list(LoanState))

    # Populate matrix based on simplified probabilities
    # This is a simplified representation based on the 'probabilities' dict.
    # A full implementation would follow Table 1 from the document.
    
    # From PER
    perf_trans = probabilities.get(LoanState.PERFORMING, {})
    matrix.loc[LoanState.PERFORMING, LoanState.PERFORMING] = perf_trans.get(LoanState.PERFORMING, 0)
    matrix.loc[LoanState.PERFORMING, LoanState.LIGHT_DELINQUENT] = perf_trans.get(LoanState.LIGHT_DELINQUENT, 0)
    matrix.loc[LoanState.PERFORMING, LoanState.PREPAY] = perf_trans.get(LoanState.PREPAY, 0)

    # From LDQ
    ldq_trans = probabilities.get(LoanState.LIGHT_DELINQUENT, {})
    matrix.loc[LoanState.LIGHT_DELINQUENT, LoanState.SERIOUSLY_DELINQUENT] = ldq_trans.get(LoanState.SERIOUSLY_DELINQUENT, 0)
    matrix.loc[LoanState.LIGHT_DELINQUENT, LoanState.REPERFORMING] = ldq_trans.get(LoanState.REPERFORMING, 0)
    matrix.loc[LoanState.LIGHT_DELINQUENT, LoanState.DEFAULT] = ldq_trans.get(LoanState.DEFAULT, 0)
    matrix.loc[LoanState.LIGHT_DELINQUENT, LoanState.PREPAY] = ldq_trans.get(LoanState.PREPAY, 0)
    
    # From SDQ
    sdq_trans = probabilities.get(LoanState.SERIOUSLY_DELINQUENT, {})
    matrix.loc[LoanState.SERIOUSLY_DELINQUENT, LoanState.DEEPLY_DELINQUENT] = sdq_trans.get(LoanState.DEEPLY_DELINQUENT, 0)
    matrix.loc[LoanState.SERIOUSLY_DELINQUENT, LoanState.REPERFORMING] = sdq_trans.get(LoanState.REPERFORMING, 0)
    matrix.loc[LoanState.SERIOUSLY_DELINQUENT, LoanState.DEFAULT] = sdq_trans.get(LoanState.DEFAULT, 0)

    # From DDQ
    ddq_trans = probabilities.get(LoanState.DEEPLY_DELINQUENT, {})
    matrix.loc[LoanState.DEEPLY_DELINQUENT, LoanState.DEEPLY_DELINQUENT] = ddq_trans.get(LoanState.DEEPLY_DELINQUENT, 0)
    matrix.loc[LoanState.DEEPLY_DELINQUENT, LoanState.REPERFORMING] = ddq_trans.get(LoanState.REPERFORMING, 0)
    matrix.loc[LoanState.DEEPLY_DELINQUENT, LoanState.DEFAULT] = ddq_trans.get(LoanState.DEFAULT, 0)

    # Terminal states
    matrix.loc[LoanState.DEFAULT, LoanState.DEFAULT] = 1.0
    matrix.loc[LoanState.PREPAY, LoanState.PREPAY] = 1.0
    
    # --- VALIDATION FIX: Correctly populate re-performing state transitions ---
    rpl_trans = probabilities.get(LoanState.REPERFORMING, {})
    matrix.loc[LoanState.REPERFORMING, LoanState.PERFORMING] = rpl_trans.get(LoanState.PERFORMING, 0)
    matrix.loc[LoanState.REPERFORMING, LoanState.LIGHT_DELINQUENT] = rpl_trans.get(LoanState.LIGHT_DELINQUENT, 0)

    mrpl_trans = probabilities.get(LoanState.MODIFIED_REPERFORMING, {})
    matrix.loc[LoanState.MODIFIED_REPERFORMING, LoanState.PERFORMING] = mrpl_trans.get(LoanState.PERFORMING, 0)
    matrix.loc[LoanState.MODIFIED_REPERFORMING, LoanState.LIGHT_DELINQUENT] = mrpl_trans.get(LoanState.LIGHT_DELINQUENT, 0)

    nrpl_trans = probabilities.get(LoanState.NON_MODIFIED_REPERFORMING, {})
    matrix.loc[LoanState.NON_MODIFIED_REPERFORMING, LoanState.PERFORMING] = nrpl_trans.get(LoanState.PERFORMING, 0)
    matrix.loc[LoanState.NON_MODIFIED_REPERFORMING, LoanState.LIGHT_DELINQUENT] = nrpl_trans.get(LoanState.LIGHT_DELINQUENT, 0)

    # Ensure rows sum to 1 (for non-terminal states)
    for state in matrix.index:
        if state not in [LoanState.DEFAULT, LoanState.PREPAY]:
            row_sum = matrix.loc[state].sum()
            if row_sum > 0 and not np.isclose(row_sum, 1.0):
                 matrix.loc[state, state] += (1.0 - row_sum) # Adjust diagonal

    return matrix
