import pandas as pd

# Read the CSV files
alpha_df = pd.read_csv("ALPHA.csv")
beta_df = pd.read_csv("BETA.csv")

# Add source indicator columns
alpha_df["ALPHA"] = "Y"
beta_df["BETA"] = "Y"

# Merge both datasets
merged_df = pd.merge(
    alpha_df,
    beta_df,
    on=["StoreID", "Date", "TransactionID", "Amount"],
    how="outer"
)

# Save the merged output
merged_df.to_csv("merged.csv", index=False)

print("Merged file saved as merged.csv")
