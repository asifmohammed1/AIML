import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from imblearn.over_sampling import RandomOverSampler
from fastapi import FastAPI

# LOAD DATASET

df = pd.read_csv("data.csv")

print("First rows of dataset:")
print(df.head())

# CHECK CLASS IMBALANCE

print("\nClass Distribution:")
print(df["strength"].value_counts())

# ENCODE LABELS

encoder = LabelEncoder()
df["strength"] = encoder.fit_transform(df["strength"])

# TEXT VECTORIZATION

vectorizer = CountVectorizer(analyzer="char")

X = vectorizer.fit_transform(df["password"])
y = df["strength"]

# TRAIN TEST SPLIT

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# HANDLE CLASS IMBALANCE

ros = RandomOverSampler(random_state=42)
X_train_resampled, y_train_resampled = ros.fit_resample(X_train, y_train)

# TRAIN MODEL

model = SVC(kernel="linear")

model.fit(X_train_resampled, y_train_resampled)

# MODEL EVALUATION

y_pred = model.predict(X_test)

print("\nModel Accuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# SAVE MODEL

pickle.dump(model, open("password_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
pickle.dump(encoder, open("encoder.pkl", "wb"))

# FASTAPI APPLICATION

app = FastAPI()

model = pickle.load(open("password_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
encoder = pickle.load(open("encoder.pkl", "rb"))


@app.get("/")
def home():
    return {"message": "Password Strength Prediction API"}


@app.post("/predict")
def predict(password: str):

    vector = vectorizer.transform([password])

    prediction = model.predict(vector)

    result = encoder.inverse_transform(prediction)

    return {
        "password": password,
        "predicted_strength": result[0]
    }


@app.post("/retrain")
def retrain():

    global model

    df = pd.read_csv("data.csv")

    encoder = LabelEncoder()
    df["strength"] = encoder.fit_transform(df["strength"])

    vectorizer = CountVectorizer(analyzer="char")

    X = vectorizer.fit_transform(df["password"])
    y = df["strength"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    ros = RandomOverSampler(random_state=42)
    X_train_resampled, y_train_resampled = ros.fit_resample(X_train, y_train)

    model = SVC(kernel="linear")
    model.fit(X_train_resampled, y_train_resampled)

    pickle.dump(model, open("password_model.pkl", "wb"))

    return {"message": "Model retrained successfully"}
