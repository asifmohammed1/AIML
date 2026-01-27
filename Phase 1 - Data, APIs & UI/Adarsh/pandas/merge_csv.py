import pandas as pd

# Step 1: Read CSV files
alpha_df = pd.read_csv("ALPHA.csv")
beta_df = pd.read_csv("BETA.csv")

# Step 2: Add indicator columns
alpha_df["ALPHA"] = "Y"
beta_df["BETA"] = "Y"

# Step 3: Merge both files
merged_df = pd.merge(
    alpha_df,
    beta_df,
    on=["StoreID", "Date", "TransactionID", "Amount"],
    how="outer"
)

# Step 4: Replace NaN with empty string
merged_df["ALPHA"] = merged_df["ALPHA"].fillna("")
merged_df["BETA"] = merged_df["BETA"].fillna("")

# Step 5: Save output
merged_df.to_csv("merged.csv", index=False)

print("merged.csv created successfully")
