import pandas as pd

# Read and print the master table
df_master = pd.read_csv("output/master_table.csv")  # change filename if needed
print("📄 Master Table")
print(df_master.to_markdown(index=False))

# Read and print the child (repeating group) table
df_children = pd.read_csv("output/child_household_members.csv")
print("\n📄 Household Members Table")
print(df_children.to_markdown(index=False))
