import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(42)

# Generate 10 sample loans
num_loans = 10

data = {
    'loan_id': range(1, num_loans + 1),
    'initial_upb': np.random.uniform(200000, 500000, num_loans).round(2),
    'current_upb': 0, # Will be initialized later
    'origination_ltv': np.random.uniform(0.80, 0.99, num_loans).round(2),
    'credit_score': np.random.randint(620, 800, num_loans),
    'loan_purpose': np.random.choice(['Purchase', 'Refinance'], size=num_loans),
    'product_type': np.random.choice(['FRM 30/40yr', 'FRM 15/20yr', 'ARM'], size=num_loans),
    'initial_state': ['PER'] * 5 + np.random.choice(['NRPL', 'LDQ', 'SDQ', 'DDQ'], size=5).tolist(),
    'base_hpi': [100.0] * num_loans # Add base_hpi column
}

loans_df = pd.DataFrame(data)

# Derive original_property_value from initial_upb and origination_ltv
loans_df['original_property_value'] = (loans_df['initial_upb'] / loans_df['origination_ltv']).round(2)

# Initialize current_upb to initial_upb
loans_df['current_upb'] = loans_df['initial_upb']

# Save to CSV
loans_df.to_csv('loans.csv', index=False)

print("Generated loans.csv with 10 sample loans.")
