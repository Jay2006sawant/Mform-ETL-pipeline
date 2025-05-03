import json
import os
import pandas as pd
from etl.transformer import flatten_submissions

def load_json_data(file_path):
    """Loads JSON data from a file."""
    print(f"Loading data from {file_path}...")
    with open(file_path, 'r') as f:
        return json.load(f)

def save_to_csv(df, file_path):
    """Saves the DataFrame to a CSV file."""
    print(f"Saving data to {file_path}...")
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    os.makedirs("output", exist_ok=True)

    print("Starting ETL process...")
    data = load_json_data("data/sample_input.json")
    
    print("Flattening submissions...")
    master_df, child_tables = flatten_submissions(data)

    print("Saving master table...")
    save_to_csv(master_df, "output/master_table.csv")
    
    # Save each child table (e.g., household members, survey responses)
    for group_name, df in child_tables.items():
        print(f"Saving {group_name} table...")
        save_to_csv(df, f"output/child_{group_name}.csv")

    print("✅ ETL completed. Check the 'output/' folder for CSVs.")
