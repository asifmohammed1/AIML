# 1. Import Required Libraries

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.utils import resample

# 2. Load Dataset

df = pd.read_csv("IMDB_Imbalanced.csv")

print("Original Class Distribution:")
print(df['sentiment'].value_counts())
print("-" * 50)


# 3. Handle Imbalance (Oversample Minority)

df_positive = df[df['sentiment'] == 'positive']
df_negative = df[df['sentiment'] == 'negative']

# Oversample minority class (negative)
df_negative_upsampled = resample(
    df_negative,
    replace=True,
    n_samples=len(df_positive),
    random_state=42
)

# Combine majority and upsampled minority
df_balanced = pd.concat([df_positive, df_negative_upsampled])

# Shuffle dataset
df_balanced = df_balanced.sample(frac=1, random_state=42).reset_index(drop=True)

print("Balanced Class Distribution:")
print(df_balanced['sentiment'].value_counts())
print("-" * 50)


# 4. Convert Text to Numerical Features

vectorizer = CountVectorizer(stop_words='english')

X = vectorizer.fit_transform(df_balanced['review'])
y = df_balanced['sentiment']

# 5. Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# 6. Train Model

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 7. Make Predictions

y_pred = model.predict(X_test)

# 8. Evaluate Model

accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)


# Original Class Distribution:
# sentiment
# positive    25000
# negative     2500
# Name: count, dtype: int64
# --------------------------------------------------
# Balanced Class Distribution:
# sentiment
# negative    25000
# positive    25000
# Name: count, dtype: int64
# Model Accuracy: 0.9808
