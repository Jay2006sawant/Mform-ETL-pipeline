import pandas as pd

def flatten_submissions(submissions):
    master_rows = []
    child_tables = {"household_members": []}

    for submission in submissions:
        # Flatten master row
        master_row = {
            "submission_id": submission["submission_id"],
            "form_name": submission["form_name"],
            "timestamp": submission["timestamp"],
            "respondent_name": submission["respondent"]["name"],
            "respondent_age": submission["respondent"]["age"],
            "respondent_gender": submission["respondent"]["gender"]
        }
        master_rows.append(master_row)

        # Extract repeat group: household_members
        for idx, member in enumerate(submission.get("household_members", [])):
            child_row = {
                "submission_id": submission["submission_id"],  # foreign key
                "member_index": idx,
                "name": member["name"],
                "age": member["age"]
            }
            child_tables["household_members"].append(child_row)

    # Convert to DataFrames
    master_df = pd.DataFrame(master_rows)
    household_df = pd.DataFrame(child_tables["household_members"])

    return master_df, {"household_members": household_df}
