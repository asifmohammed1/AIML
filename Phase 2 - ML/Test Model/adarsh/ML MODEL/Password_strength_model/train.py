# Import required libraries
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
import joblib


# 1 Load dataset
data = pd.read_csv("dataset.csv")

print("First 5 rows of dataset:")
print(data.head())


# 2 Check class imbalance
print("\nClass Distribution:")
print(data["strength"].value_counts())


# 3 Separate input and output
X = data["password"]
y = data["strength"]


# 4 Convert text to numbers
vectorizer = CountVectorizer(analyzer="char")

X_vectorized = vectorizer.fit_transform(X)


# 5 Handle class imbalance
ros = RandomOverSampler()

X_resampled, y_resampled = ros.fit_resample(X_vectorized, y)


# 6 Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_resampled, y_resampled, test_size=0.2, random_state=42
)


# 7 Train model
model = SVC()

model.fit(X_train, y_train)


# 8 Prediction
y_pred = model.predict(X_test)


# 9 Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)


# 10 Save model
joblib.dump(model, "password_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("\nModel saved successfully")
