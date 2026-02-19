import pandas as pd
import numpy as np


#  TASK 1: LOAD DATA SAFELY (HANDLE DELIMITER ISSUES)

clean_rows = []

with open("Unclean Dataset.csv", "r", encoding="latin1") as f:
    for line in f:
        parts = line.strip().split("|")

        # Only keep rows with at least 8 values
        if len(parts) >= 8:
            clean_rows.append(parts[:8])  # Take first 8 only

# Create DataFrame
df = pd.DataFrame(clean_rows, columns=[
    "Student_ID",
    "First_Name",
    "Last_Name",
    "Age",
    "Gender",
    "Course",
    "Enrollment_Date",
    "Total_Payments"
])

print("Raw Shape:", df.shape)



#  TASK 2: FIX COLUMN STRUCTURE & CLEAN SPACES


df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)



#  TASK 3: HANDLE MISSING VALUES


df.replace(["NA", "na", "", " ", "null", "?"], np.nan, inplace=True)

# Age → median
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Age"] = df["Age"].fillna(df["Age"].median())

# Course → Unknown
df["Course"] = df["Course"].fillna("Unknown")

# Enrollment_Date → mode
if not df["Enrollment_Date"].mode().empty:
    df["Enrollment_Date"] = df["Enrollment_Date"].fillna(
        df["Enrollment_Date"].mode()[0]
    )



#  TASK 4: REMOVE DUPLICATES


df = df.drop_duplicates(subset=["Student_ID"])

df = df.drop_duplicates(
    subset=["First_Name", "Last_Name", "Enrollment_Date"]
)


#  TASK 5: DATA TYPE CLEANING


# Student_ID → integer
df["Student_ID"] = pd.to_numeric(df["Student_ID"], errors="coerce")
df = df.dropna(subset=["Student_ID"])
df["Student_ID"] = df["Student_ID"].astype(int)

# Age → integer
df["Age"] = df["Age"].astype(int)

# Clean Total_Payments
df["Total_Payments"] = (
    df["Total_Payments"]
    .astype(str)
    .str.replace(r"[$,?]", "", regex=True)
)

df["Total_Payments"] = pd.to_numeric(
    df["Total_Payments"], errors="coerce"
)

# Fill missing payments with median
df["Total_Payments"] = df["Total_Payments"].fillna(
    df["Total_Payments"].median()
)

# Enrollment_Date → datetime
df["Enrollment_Date"] = pd.to_datetime(df["Enrollment_Date"])


#  TASK 6: STANDARDIZATION


df["Course"] = df["Course"].replace({
    "Machine Learnin": "Machine Learning",
    "Web Developmen": "Web Development",
    "Web Developmet": "Web Development"
})

df["Gender"] = df["Gender"].str.upper().str.strip()

df["Gender"] = df["Gender"].replace({
    "MALE": "M",
    "FEMALE": "F"
})

df["First_Name"] = df["First_Name"].str.strip()
df["Last_Name"] = df["Last_Name"].str.strip()
df["Course"] = df["Course"].str.strip()

#  TASK 7: FINAL OUTPUT

df.to_csv("Cleaned_Student_Enrollment_Dataset.csv", index=False)

print("\n DATA CLEANING COMPLETED SUCCESSFULLY")
print("Final Shape:", df.shape)
print("\nFinal Data Types:")
print(df.dtypes)
print("\nCleaned Preview:")
print(df.head())
