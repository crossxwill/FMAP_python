import subprocess
import sys

# List of scripts to run in order
scripts = [
    "01_generate_loans_data.py",
    "02_generate_mev_scenarios.py",
    "03_simulate_cash_flows.py",
    "04_simulate_markov_chain.py",
    "05_simulate_monte_carlo.py",
    "06_compare_simulations.py"
]

def run_script(script_name):
    """Runs a python script and checks for errors."""
    print(f"--- Running {script_name} ---")
    try:
        process = subprocess.run(
            [sys.executable, script_name],
            check=True,
            capture_output=True,
            text=True
        )
        print(process.stdout)
        if process.stderr:
            print("Error output:")
            print(process.stderr)
        print(f"--- Finished {script_name} successfully ---\n")
        return True
    except subprocess.CalledProcessError as e:
        print(f"!!! ERROR running {script_name} !!!")
        print(f"Return Code: {e.returncode}")
        print("--- STDOUT ---")
        print(e.stdout)
        print("--- STDERR ---")
        print(e.stderr)
        return False

def main():
    """Main function to run all scripts."""
    print("========================================")
    print("=   FMAP Credit Loss Simulation Suite  =")
    print("========================================")
    
    for script in scripts:
        if not run_script(script):
            print(f"\nExecution stopped due to an error in {script}.")
            sys.exit(1) # Exit with an error code
            
    print("========================================")
    print("=      All scripts ran successfully!   =")
    print("========================================")

if __name__ == "__main__":
    main()
