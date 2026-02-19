import pandas as pd
import numpy as np
import re

# STEP 1: Rebuild structure

clean_records = []

with open("Unclean Dataset.csv", "r", encoding="latin1") as f:
    for line in f:
        line = line.replace("|", ",")
        line = re.sub(r"\s+", " ", line)

        parts = [p.strip() for p in line.split(",") if p.strip() != ""]

        # Process every 8 values as one student record
        for i in range(0, len(parts), 8):
            chunk = parts[i:i+8]

            if len(chunk) == 8:
                try:
                    int(chunk[0])  # Check Student_ID is numeric
                    clean_records.append(chunk)
                except:
                    continue

print("Reconstructed records:", len(clean_records))

df = pd.DataFrame(clean_records, columns=[
    "Student_ID",
    "First_Name",
    "Last_Name",
    "Age",
    "Gender",
    "Course",
    "Enrollment_Date",
    "Total_Payments"
])

# STEP 2: Basic Cleaning

df = df.apply(lambda x: x.astype(str).str.strip())

df.replace(["NA", "", "nan", "None"], np.nan, inplace=True)

# STEP 3: Fix Data Types

df["Student_ID"] = pd.to_numeric(df["Student_ID"], errors="coerce")

df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Age"].fillna(df["Age"].median(), inplace=True)
df["Age"] = df["Age"].astype(int)

df["Total_Payments"] = df["Total_Payments"].str.replace(r"[^\d.]", "", regex=True)
df["Total_Payments"] = pd.to_numeric(df["Total_Payments"], errors="coerce")

df["Enrollment_Date"] = pd.to_datetime(df["Enrollment_Date"], errors="coerce")
df["Enrollment_Date"].fillna(df["Enrollment_Date"].mode()[0], inplace=True)

# STEP 4: Standardization

df["Course"] = df["Course"].replace({
    "Machine Learnin": "Machine Learning",
    "Web Developmen": "Web Development"
})

df["Course"].fillna("Unknown", inplace=True)

df["Gender"] = df["Gender"].str.upper().replace({
    "MALE": "M",
    "FEMALE": "F"
})

print("After reconstruction:", len(df))

# STEP 5: Remove TRUE duplicates

df.drop_duplicates(
    subset=["First_Name", "Last_Name", "Enrollment_Date"],
    inplace=True
)
print("After removing duplicates:", len(df))

# STEP 6: Sort for neatness

df.sort_values("Student_ID", inplace=True)

# STEP 7: Save final file

df.to_csv("Cleaned_Dataset.csv", index=False)

print("Final cleaned dataset created.")
print("Final row count:", len(df))

print(len(df))
print(df["Student_ID"].nunique())

print(df[["Student_ID","First_Name","Last_Name"]])

