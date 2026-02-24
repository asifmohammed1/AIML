# STEP 1: IMPORT REQUIRED LIBRARIES

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.utils import resample

# STEP 2: LOAD IMBALANCED DATASET

df = pd.read_csv("IMDB_Imbalanced.csv")

print("First 5 rows:")
print(df.head())

print("\nClass Distribution BEFORE Balancing:")
print(df["sentiment"].value_counts())


# STEP 3: HANDLE CLASS IMBALANCE (OVER-SAMPLING)

# Separate majority and minority classes
majority_class = df[df["sentiment"] == df["sentiment"].value_counts().idxmax()]
minority_class = df[df["sentiment"] == df["sentiment"].value_counts().idxmin()]

# Over-sample minority class
minority_upsampled = resample(
    minority_class,
    replace=True,
    n_samples=len(majority_class),
    random_state=42
)

# Combine classes
df_balanced = pd.concat([majority_class, minority_upsampled])

print("\nClass Distribution AFTER Balancing:")
print(df_balanced["sentiment"].value_counts())


# STEP 4: SPLIT DATA INTO TRAIN & TEST SETS

X = df_balanced["review"]      # text column
y = df_balanced["sentiment"]   # label column

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# STEP 5: CONVERT TEXT TO NUMERICAL FEATURES

vectorizer = CountVectorizer(stop_words="english")

X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)


# STEP 6: TRAIN SUPERVISED MODEL

model = LogisticRegression(max_iter=1000)

model.fit(X_train_vectorized, y_train)


# STEP 7: MODEL EVALUATION

y_pred = model.predict(X_test_vectorized)

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# I SHARED MY ACCURACY AND REPORTS JUST BELOW


# Class Distribution BEFORE Balancing:
# sentiment
# positive    25000
# negative     2500
# Name: count, dtype: int64

# Class Distribution AFTER Balancing:
# sentiment
# positive    25000
# negative    25000
# Name: count, dtype: int64

# Model Accuracy: 0.9803

# Classification Report:
#               precision    recall  f1-score   support

#     negative       0.96      1.00      0.98      4978
#     positive       1.00      0.96      0.98      5022

#     accuracy                           0.98     10000
#    macro avg       0.98      0.98      0.98     10000
# weighted avg       0.98      0.98      0.98     10000

