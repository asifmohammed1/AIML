import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.utils import resample
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report


print("--- Step 1: Load and Prepare Data ---")
df = pd.read_csv("Reviews.csv")

# Keep only necessary columns and drop NA
df = df[['Text', 'Score']].dropna()

# Remove neutral 3-star reviews
df = df[df['Score'] != 3]

# Convert to binary labels
df['label'] = df['Score'].apply(lambda x: 'positive' if x > 3 else 'negative')
df = df.rename(columns={'Text': 'text'})

print("\nOriginal Dataset Distribution:")
print(df['label'].value_counts())
print("-" * 50)

X = df['text']
y = df['label']

print("Splitting data into train and test sets...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

print("\n--- Step 2: Balance the Training Data ---")
train_data = pd.DataFrame({'text': X_train, 'label': y_train})

majority = train_data[train_data['label'] == 'positive']
minority = train_data[train_data['label'] == 'negative']

print("Upsampling the minority class...")
minority_upsampled = resample(minority, 
                              replace=True,               
                              n_samples=len(majority),    
                              random_state=42)            

balanced_train_data = pd.concat([majority, minority_upsampled])

X_train_balanced = balanced_train_data['text']
y_train_balanced = balanced_train_data['label']

print("Balanced Training Set Distribution:")
print(y_train_balanced.value_counts())
print("-" * 50)

print("\n--- Step 3: Vectorization (Supercharged CountVectorizer) ---")
print("Extracting Bigrams and removing Stop Words...")

# This is the secret to higher accuracy using only CountVectorizer!
vectorizer = CountVectorizer(
    stop_words='english',   
    ngram_range=(1, 2),     
    max_features=15000,    
    min_df=5               
)

# Fit and transform the balanced training data
X_train_vec = vectorizer.fit_transform(X_train_balanced)

# Transform the test data
X_test_vec = vectorizer.transform(X_test)

print("\n--- Step 4: Model Training ---")
print("Training the Multinomial Naive Bayes model...")
model = MultinomialNB()
model.fit(X_train_vec, y_train_balanced)

print("\n--- Step 5: Model Evaluation ---")
y_pred = model.predict(X_test_vec)

accuracy = accuracy_score(y_test, y_pred)

print(f"\nFinal Accuracy Score: {accuracy:.4f}")
print("\nDetailed Classification Report:")
print(classification_report(y_test, y_pred))
'''Original Dataset Distribution:
label
positive    443777
negative     82037
Name: count, dtype: int64
--------------------------------------------------
Splitting data into train and test sets...

--- Step 2: Balance the Training Data ---
Upsampling the minority class...
Balanced Training Set Distribution:
label
positive    310643
negative    310643
Name: count, dtype: int64
--------------------------------------------------

--- Step 3: Vectorization (Supercharged CountVectorizer) ---
Extracting Bigrams and removing Stop Words...

--- Step 4: Model Training ---
Training the Multinomial Naive Bayes model...

--- Step 5: Model Evaluation ---

Final Accuracy Score: 0.8991

Detailed Classification Report:
              precision    recall  f1-score   support

    negative       0.63      0.83      0.72     24611
    positive       0.97      0.91      0.94    133134

    accuracy                           0.90    157745
   macro avg       0.80      0.87      0.83    157745
weighted avg       0.92      0.90      0.90    157745
'''