import pandas as pd
import numpy as np
import re

# Step 1: Reconstruct valid rows
clean_records = []

with open("Unclean Dataset.csv", "r", encoding="latin1") as f:
    # Skip the header to avoid parsing it as data
    lines = f.readlines()[1:]
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Replace | with comma to unify delimiters
        line = line.replace("|", ",")

        # Remove extra spaces
        line = re.sub(r"\s+", " ", line)

        # Split values and drop empty strings (clears out trailing commas)
        parts = [p.strip() for p in line.split(",") if p.strip() != ""]

        # Brilliant chunking logic to handle horizontally merged rows
        for i in range(0, len(parts), 8):
            chunk = parts[i:i+8]

            if len(chunk) != 8:
                continue

            # We DO NOT use strict try/except here. We want to KEEP rows 
            # with "NA" or missing values so we can fill them in Step 3!
            clean_records.append(chunk)

print("Valid reconstructed records:", len(clean_records))

# Create DataFrame
df = pd.DataFrame(clean_records, columns=[
    "Student_ID", "First_Name", "Last_Name", "Age",
    "Gender", "Course", "Enrollment_Date", "Total_Payments"
])

# Step 2: Clean basic values
df = df.apply(lambda x: x.astype(str).str.strip())
df.replace(["NA", "na", "", "nan", "None", "?"], np.nan, inplace=True)

# Step 3: Fix data types & Fill Missing Values
# Student ID
df["Student_ID"] = pd.to_numeric(df["Student_ID"], errors="coerce")
df.dropna(subset=["Student_ID"], inplace=True)
df["Student_ID"] = df["Student_ID"].astype(int)

# Age -> Fill median
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Age"] = df["Age"].fillna(df["Age"].median()).astype(int)

# Total Payments -> Clean symbols and convert to Integer
df["Total_Payments"] = df["Total_Payments"].str.replace(r"[^\d.]", "", regex=True)
df["Total_Payments"] = pd.to_numeric(df["Total_Payments"], errors="coerce").round().astype('Int64')

# Enrollment Date -> Fill mode
df["Enrollment_Date"] = pd.to_datetime(df["Enrollment_Date"], errors="coerce")
if not df["Enrollment_Date"].mode().empty:
    df["Enrollment_Date"] = df["Enrollment_Date"].fillna(df["Enrollment_Date"].mode()[0])
df["Enrollment_Date"] = df["Enrollment_Date"].dt.strftime('%Y-%m-%d')

# Step 4: Standardize text
df["Course"] = df["Course"].replace({
    "Machine Learnin": "Machine Learning",
    "Web Developmen": "Web Development",
    "Web Developmet": "Web Development"
})
df["Course"] = df["Course"].fillna("Unknown")

df["Gender"] = df["Gender"].str.upper().replace({
    "MALE": "M",
    "FEMALE": "F"
})

# Keep only valid M/F genders
df.loc[~df["Gender"].isin(["M", "F"]), "Gender"] = np.nan

# Step 5: Remove true duplicates
# We drop based on Name & Date to avoid dropping different students sharing a broken ID
df.drop_duplicates(
    subset=["First_Name", "Last_Name", "Enrollment_Date"],
    keep="first",
    inplace=True
)

# Step 6: Sort neatly
df.sort_values("Student_ID", inplace=True)

# Step 7: Export final file
df.to_csv("Cleaned_Dataset.csv", index=False)

print("✅ Cleaning completed successfully.")
print("Final row count:", len(df))
print("Unique courses:", df["Course"].nunique())