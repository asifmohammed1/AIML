import pandas as pd
import numpy as np
import re

# Step 1: Reconstruct valid rows

clean_records = []

with open("Unclean Dataset.csv", "r", encoding="latin1") as f:
    for line in f:
        # Replace | with comma just in case
        line = line.replace("|", ",")

        # Remove extra spaces
        line = re.sub(r"\s+", " ", line)

        # Split values
        parts = [p.strip() for p in line.split(",") if p.strip() != ""]

        # Some lines contain more than one student
        # So we process in chunks of 8
        for i in range(0, len(parts), 8):
            chunk = parts[i:i+8]

            if len(chunk) != 8:
                continue

            try:
                # Validate basic structure before accepting

                student_id = int(chunk[0])
                age = int(chunk[3])
                gender = chunk[4].upper()

                if gender not in ["M", "F"]:
                    continue

                # Validate date
                pd.to_datetime(chunk[6], errors="raise")

                # Validate payment
                payment = re.sub(r"[^\d.]", "", chunk[7])
                float(payment)

                clean_records.append(chunk)

            except:
                # Skip broken rows silently
                continue

print("Valid reconstructed records:", len(clean_records))

# Create DataFrame
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

# Step 2: Clean basic values

df = df.apply(lambda x: x.astype(str).str.strip())

df.replace(["NA", "", "nan", "None"], np.nan, inplace=True)

# Step 3: Fix data types

df["Student_ID"] = pd.to_numeric(df["Student_ID"], errors="coerce")

df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Age"].fillna(df["Age"].median(), inplace=True)
df["Age"] = df["Age"].astype(int)

# Clean payment column
df["Total_Payments"] = df["Total_Payments"].str.replace(r"[^\d.]", "", regex=True)
df["Total_Payments"] = pd.to_numeric(df["Total_Payments"], errors="coerce")

# Fix dates
df["Enrollment_Date"] = pd.to_datetime(df["Enrollment_Date"], errors="coerce")
df["Enrollment_Date"].fillna(df["Enrollment_Date"].mode()[0], inplace=True)

# Step 4: Standardize text

df["Course"] = df["Course"].replace({
    "Machine Learnin": "Machine Learning",
    "Web Developmen": "Web Development"
})

df["Course"].fillna("Unknown", inplace=True)

df["Gender"] = df["Gender"].str.upper().replace({
    "MALE": "M",
    "FEMALE": "F"
})

# Step 5: Remove true duplicates

df.drop_duplicates(
    subset=["First_Name", "Last_Name", "Enrollment_Date"],
    inplace=True
)

# Step 6: Sort neatly

df.sort_values("Student_ID", inplace=True)

# Step 7: Export final file

df.to_csv("Cleaned_Dataset.csv", index=False)

print("Cleaning completed.")
print("Final row count:", len(df))
print("Unique courses:", df["Course"].nunique())
