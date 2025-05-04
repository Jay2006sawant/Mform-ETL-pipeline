import os
import requests
import pandas as pd
from tabulate import tabulate

# Ensure output directory exists
os.makedirs("output", exist_ok=True)

# Fetch data from the public nested JSON API
url = "https://randomuser.me/api/?results=3"
response = requests.get(url)
data = response.json()

# Prepare master and child data
master_data = []
child_data = []

for user in data["results"]:
    user_id = user["login"]["uuid"]

    master_data.append({
        "uuid": user_id,
        "first_name": user["name"]["first"],
        "last_name": user["name"]["last"],
        "email": user["email"],
        "phone": user["phone"],
        "gender": user["gender"],
        "dob": user["dob"]["date"]
    })

    child_data.append({
        "uuid": user_id,
        "street": f'{user["location"]["street"]["number"]} {user["location"]["street"]["name"]}',
        "city": user["location"]["city"],
        "state": user["location"]["state"],
        "country": user["location"]["country"],
        "postcode": user["location"]["postcode"],
        "latitude": user["location"]["coordinates"]["latitude"],
        "longitude": user["location"]["coordinates"]["longitude"]
    })

# Convert to DataFrames
df_master = pd.DataFrame(master_data)
df_child = pd.DataFrame(child_data)

# Export to CSV
df_master.to_csv("output/master_random_users.csv", index=False)
df_child.to_csv("output/child_locations.csv", index=False)

# Print the data in tabular format
print("✅ Data extraction and transformation completed.")
print("📄 Files saved in 'output/' folder:")
print(" - master_random_users.csv")
print(" - child_locations.csv")

# Display the master table
print("\n📄 Master Table:")
print(tabulate(df_master, headers='keys', tablefmt='grid', showindex=False))

# Display the child table
print("\n📄 Child Table (Locations):")
print(tabulate(df_child, headers='keys', tablefmt='grid', showindex=False))
