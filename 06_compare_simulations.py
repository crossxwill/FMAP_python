
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Data
try:
    cashflow_df = pd.read_csv('cashflow_results.csv')
    markov_df = pd.read_csv('markov_chain_results.csv')
    monte_carlo_df = pd.read_csv('monte_carlo_results.csv')
except FileNotFoundError as e:
    print(f"Error: {e}. Please ensure all simulation scripts have been run successfully.")
    exit()

# 2. Aggregate Losses
# Group by scenario and sum the relevant loss column
cashflow_agg = cashflow_df.groupby('scenario_id')['credit_loss'].sum()
markov_agg = markov_df.groupby('scenario_id')['expected_credit_loss'].sum()
monte_carlo_agg = monte_carlo_df.groupby('scenario_id')['credit_loss'].sum()

# 3. Combine and Display
# Create a summary DataFrame
summary_df = pd.DataFrame({
    'Cashflow_Total_Loss': cashflow_agg,
    'MarkovChain_Total_Loss': markov_agg,
    'MonteCarlo_Total_Loss': monte_carlo_agg
})

print("--- Total Portfolio Loss by Scenario and Simulation Method ---")
print(summary_df)

# 4. Visualize Results
# Reset index to make 'scenario_id' a column for plotting
plot_df = summary_df.reset_index().melt(
    id_vars='scenario_id', 
    var_name='Simulation_Method', 
    value_name='Total_Loss'
)

plt.figure(figsize=(12, 7))
sns.barplot(data=plot_df, x='scenario_id', y='Total_Loss', hue='Simulation_Method')

plt.title('Comparison of Total Simulated Credit Losses by Scenario')
plt.xlabel('Scenario')
plt.ylabel('Total Aggregated Credit Loss ($)')
plt.ticklabel_format(style='plain', axis='y') # Prevent scientific notation
plt.legend(title='Simulation Method')
plt.tight_layout()

# Save the plot to a file
plt.savefig('simulation_comparison.png')
print("\nComparison chart saved to simulation_comparison.png")

plt.show()
