import os
import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

DATA_PATH = "data.csv"
TFIDF_PATH = "tfidf.pkl"

app = FastAPI()

# ---------- Models ----------
class ChatData(BaseModel):
    question: str
    answer: str

# ---------- Load CSV ----------
def load_data():
    return pd.read_csv(DATA_PATH, encoding="utf-8", on_bad_lines="skip")

df = load_data()

# ---------- Train Model ----------
def train_model():
    global model, tfidf, df
    df = load_data()

    X = df["question"]
    y = df.index

    tfidf = TfidfVectorizer(lowercase=True)
    X_vec = tfidf.fit_transform(X)

    model = LinearSVC()
    model.fit(X_vec, y)

    with open(TFIDF_PATH, "wb") as f:
        pickle.dump(tfidf, f)

# ---------- Load Model ----------
def load_model():
    global model, tfidf
    try:
        if os.path.exists(MODEL_PATH) and os.path.exists(TFIDF_PATH):
            with open(MODEL_PATH, "rb") as f:
                model = pickle.load(f)
            with open(TFIDF_PATH, "rb") as f:
                tfidf = pickle.load(f)
        else:
            raise Exception("Model files not found")
    except Exception as e:
        print("Model load failed, retraining...", e)
        train_model()

load_model()

# ---------- APIs ----------

# Chat API
@app.get("/chat")
def chat(message: str):
    vec = tfidf.transform([message])
    pred = model.predict(vec)[0]
    answer = df.iloc[pred]["answer"]
    return {"question": message, "answer": answer}

# Add new data API
@app.post("/add-data")
def add_data(data: ChatData):
    global df
    df = load_data()

    new_row = pd.DataFrame([[data.question, data.answer]],
                           columns=["question", "answer"])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(DATA_PATH, index=False)

    return {"message": "Data added successfully"}

# Retrain & export model API
@app.post("/train")
def retrain():
    train_model()
    return {"message": "Model retrained and exported successfully"}
