import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import RandomOverSampler
import uvicorn

# Initialize FastAPI
app = FastAPI(title="Password Strength Classifier")

# --- Global Variables ---
# analyzer='char' breaks passwords into character chunks (better for patterns)
# C=0.5 prevents the model from being "too perfect" (overfitting)
vectorizer = CountVectorizer(analyzer='char', ngram_range=(2, 3))
model = SVC(kernel='linear', C=0.5)

def train_pipeline():
    global model, vectorizer
    
    # 1. Load Dataset
    # Ensure 'passwords.csv' is in the same folder
    df = pd.read_csv('data.csv')
    df.columns = df.columns.str.strip() # Clean column names
    
    # 2. Vectorize
    X = vectorizer.fit_transform(df['password'].values.astype('U'))
    y = df['strength']
    
    # 3. Train/Test Split (The key to getting ~95% instead of 100%)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42
    )
    
    # 4. Handle Imbalance (OverSampling)
    ros = RandomOverSampler(random_state=42)
    X_resampled, y_resampled = ros.fit_resample(X_train, y_train)
    
    # 5. Train the SVC Model
    model.fit(X_resampled, y_resampled)
    
    # 6. Evaluate on Unseen Data
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    
    print(f"\n--- Model Training Complete ---")
    print(f"Validation Accuracy: {acc:.2%}")
    print(f"Balanced Classes: {pd.Series(y_resampled).value_counts().to_dict()}\n")
    
    return acc

# Initial training on startup
try:
    current_accuracy = train_pipeline()
except Exception as e:
    print(f"Startup Error: {e}")
    current_accuracy = 0

# --- API Models ---
class PasswordRequest(BaseModel):
    password: str

# --- Endpoints ---
@app.get("/")
def home():
    return {
        "status": "Online",
        "model_accuracy": f"{current_accuracy:.2%}",
        "instructions": "Go to /docs for the interactive UI"
    }

@app.post("/predict")
async def predict(request: PasswordRequest):
    # Transform user input
    vec_input = vectorizer.transform([request.password])
    prediction = model.predict(vec_input)[0]
    
    return {
        "password": request.password,
        "strength_prediction": str(prediction)
    }

@app.post("/retrain")
async def retrain():
    global current_accuracy
    current_accuracy = train_pipeline()
    return {
        "message": "Model retrained successfully",
        "new_accuracy": f"{current_accuracy:.2%}"
    }

if __name__ == "__main__":
    # Use 127.0.0.1 for local Windows access
    print("Starting server... Access UI at http://127.0.0.1:8000/docs")

    uvicorn.run(app, host="127.0.0.1", port=8000)


#output:
--- Model Training Complete ---
Validation Accuracy: 89.47%
Balanced Classes: {'weak': 58, 'strong': 58, 'medium': 58}
