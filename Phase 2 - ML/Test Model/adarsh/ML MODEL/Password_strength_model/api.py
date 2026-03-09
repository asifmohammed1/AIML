from fastapi import FastAPI
import joblib

# Load model and vectorizer
model = joblib.load("password_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Password Strength Predictor API"}


@app.post("/predict")
def predict(password: str):

    # Convert password to vector
    password_vector = vectorizer.transform([password])

    # Predict strength
    prediction = model.predict(password_vector)

    return {"password": password, "strength": prediction[0]}