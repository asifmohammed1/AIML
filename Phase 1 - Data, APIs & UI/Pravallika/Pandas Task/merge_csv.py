import pandas as pd

# Load CSV files
alpha_df = pd.read_csv("ALPHA.csv")
beta_df = pd.read_csv("BETA.csv")

# Add indicator columns
alpha_df["ALPHA"] = "Y"
beta_df["BETA"] = "Y"

# Merge using outer join
merged_df = pd.merge(
    alpha_df,
    beta_df,
    on=["StoreID", "Date", "TransactionID", "Amount"],
    how="outer"
)

merged["ALPHA"] = merged["ALPHA"].fillna("")
merged["BETA"] = merged["BETA"].fillna("")

# Save output
merged_df.to_csv("merged.csv", index=False)

print("Merged file saved as merged.csv")
