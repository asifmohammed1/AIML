import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# Global variables to hold our model and vectorizer in memory
model = None
vectorizer = None

# Create the FastAPI app
app = FastAPI(title="Password Strength / Text Classifier API")

# Request Schemas
class TextRequest(BaseModel):
    text: str

def load_and_train_model():
    """Handles the entire Scikit-Learn workflow requested."""
    global model, vectorizer
    
    print("--- 1. Loading Dataset ---")
    # Load dataset
    df = pd.read_csv("data.csv").dropna()
    
    # Use password for text, strength for label
    X = df['password'].astype(str)
    y = df['strength']

    print("\n--- 2. Checking Class Imbalance ---")
    print(df['strength'].value_counts())

    # Split data FIRST before balancing to prevent data leakage
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    print("\n--- 3. Converting Text using CountVectorizer ---")
    # Using character analyzer since passwords don't have words
    vectorizer = CountVectorizer(analyzer='char', ngram_range=(1, 3))
    
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    print("\n--- 4. Applying Resampling ---")
    # Applying RandomOverSampler (You can swap this with RandomUnderSampler if preferred)
    ros = RandomOverSampler(random_state=42)
    X_train_resampled, y_train_resampled = ros.fit_resample(X_train_vec, y_train)
    
    print("Class Distribution AFTER Over-Sampling:")
    print(pd.Series(y_train_resampled).value_counts())
    
    # NOTE: If you wanted to use Under-Sampling instead, you would use:
    # rus = RandomUnderSampler(random_state=42)
    # X_train_resampled, y_train_resampled = rus.fit_resample(X_train_vec, y_train)

    print("\n--- 5. Training Support Vector Classifier (SVC) ---")
    model = SVC(kernel='linear', random_state=42)
    model.fit(X_train_resampled, y_train_resampled)

    print("\n--- 6. Evaluating Model Accuracy ---")
    y_pred = model.predict(X_test_vec)
    acc = accuracy_score(y_test, y_pred)
    
    print(f"Model Accuracy: {acc * 100:.2f}%\n")
    print(classification_report(y_test, y_pred))
    
    return acc



@app.on_event("startup")
def startup_event():
    """Trains the model automatically when the server starts."""
    print("Starting up and training the model...")
    load_and_train_model()

@app.post("/predict")
def predict_strength(request: TextRequest):
    """Endpoint to predict the strength of a new password/text."""
    if not model or not vectorizer:
        return {"error": "Model is not trained yet."}
    
    # Vectorize the incoming text
    text_vec = vectorizer.transform([request.text])
    
    # Predict using the SVC model
    prediction = model.predict(text_vec)[0]
    
    return {
        "input_text": request.text,
        "predicted_class": prediction
    }

@app.post("/retrain")
def retrain_model():
    """Endpoint to retrain the model on the fly."""
    acc = load_and_train_model()
    return {"message": "Model retrained successfully!", "new_accuracy": acc}

if __name__ == "__main__":
    # Runs the FastAPI server locally on port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)
    '''
    Starting up and training the model...
--- 1. Loading Dataset ---

--- 2. Checking Class Imbalance ---
strength
strong    70
weak      60
medium    59
Name: count, dtype: int64

--- 3. Converting Text using CountVectorizer ---

--- 4. Applying Resampling ---
Class Distribution AFTER Over-Sampling:
strength
medium    56
strong    56
weak      56
Name: count, dtype: int64

--- 5. Training Support Vector Classifier (SVC) ---

--- 6. Evaluating Model Accuracy ---
Model Accuracy: 97.37%

              precision    recall  f1-score   support

      strong       1.00      0.93      0.96        14
        weak       0.92      1.00      0.96        12

    accuracy                           0.97        38
   macro avg       0.97      0.98      0.97        38
weighted avg       0.98      0.97      0.97        38'''