import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.utils import resample
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# --- Step 1: Load and Prepare Data ---
# Note: Ensure 'IMDB Dataset.csv' is in your directory
df = pd.read_csv("IMDB Dataset.csv")

# IMDb usually has 'review' (text) and 'sentiment' (positive/negative)
df = df.rename(columns={'review': 'text', 'sentiment': 'label'})

print("Dataset Preview:")
print(df.head())

print("\nOriginal Distribution:")
print(df['label'].value_counts())

# --- Step 2: Split and Balance ---
X = df['text']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Combine training features and labels for resampling
train_data = pd.DataFrame({'text': X_train, 'label': y_train})

# Upsampling logic (Handles any potential imbalance)
majority = train_data[train_data['label'] == 'positive']
minority = train_data[train_data['label'] == 'negative']

if len(majority) != len(minority):
    print("\nBalancing classes...")
    minority_upsampled = resample(minority, 
                                  replace=True, 
                                  n_samples=len(majority), 
                                  random_state=42)
    balanced_train_data = pd.concat([majority, minority_upsampled])
else:
    balanced_train_data = train_data

X_train_balanced = balanced_train_data['text']
y_train_balanced = balanced_train_data['label']

# --- Step 3: Supercharged Vectorization ---
# Movies have richer vocab; we'll keep the bigrams for "plot twist" or "not worth"
vectorizer = CountVectorizer(
    stop_words='english',
    ngram_range=(1, 2),
    max_features=20000, # Increased for larger movie vocabulary
    min_df=5
)

X_train_vec = vectorizer.fit_transform(X_train_balanced)
X_test_vec = vectorizer.transform(X_test)

# --- Step 4: Training & Evaluation ---
model = MultinomialNB()
model.fit(X_train_vec, y_train_balanced)

y_pred = model.predict(X_test_vec)

print(f"\nFinal Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print("\nClassification Report:")

print(classification_report(y_test, y_pred))

# output:
Original Distribution:
label
positive    25000
negative    25000
Name: count, dtype: int64

Final Accuracy: 0.8608

Classification Report:
              precision    recall  f1-score   support

    negative       0.86      0.86      0.86      5000
    positive       0.86      0.86      0.86      5000

    accuracy                           0.86     10000
   macro avg       0.86      0.86      0.86     10000
weighted avg       0.86      0.86      0.86     10000
