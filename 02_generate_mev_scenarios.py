import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(42)

# Define a 60-month forecast horizon
forecast_horizon = 60
months = range(1, forecast_horizon + 1)

# --- Normal Scenario ---
normal_hpi = 150 * (1 + 0.003) ** np.arange(forecast_horizon)
normal_unemployment = np.linspace(4.5, 4.0, forecast_horizon)
normal_interest_rate = np.linspace(3.5, 4.0, forecast_horizon)

normal_df = pd.DataFrame({
    'month': months,
    'scenario_id': 'Normal',
    'hpi_index': normal_hpi,
    'unemployment_rate': normal_unemployment,
    'interest_rate': normal_interest_rate
})

# --- Recession Scenario ---
# Simulate a sharp drop and slow recovery in HPI
recession_hpi = 150 * (1 - 0.01) ** np.arange(forecast_horizon)
recession_hpi[12:36] = recession_hpi[12] * (1 - 0.015) ** np.arange(24) # Steeper drop

recession_unemployment = np.linspace(5.0, 8.5, forecast_horizon)
recession_interest_rate = np.linspace(3.0, 2.0, forecast_horizon)

recession_df = pd.DataFrame({
    'month': months,
    'scenario_id': 'Recession',
    'hpi_index': recession_hpi,
    'unemployment_rate': recession_unemployment,
    'interest_rate': recession_interest_rate
})

# Combine scenarios and save to CSV
scenarios_df = pd.concat([normal_df, recession_df], ignore_index=True)
scenarios_df.to_csv('scenarios.csv', index=False)

print("Generated scenarios.csv with Normal and Recession scenarios for 60 months.")
