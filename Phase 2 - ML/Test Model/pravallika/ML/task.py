import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import RandomOverSampler

# Load dataset
df = pd.read_csv("data.csv")

print("Columns:", df.columns)
print(df.head())

# Check class imbalance
print("\nClass Distribution:")
print(df['strength'].value_counts())

# Convert text to numeric
vectorizer = CountVectorizer()

X = vectorizer.fit_transform(df['password'])
y = df['strength']

# Oversampling
ros = RandomOverSampler(random_state=42)
X_over, y_over = ros.fit_resample(X, y)

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X_over, y_over, test_size=0.2, random_state=42
)

# Train model
model = SVC()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)


print("\nModel Accuracy:", accuracy)





#output:
Columns: Index(['password', 'strength'], dtype='object')
   password strength
0    123456     weak
1  password     weak
2    qwerty     weak
3    111111     weak
4    abc123     weak

Class Distribution:
strength
strong    70
weak      60
medium    59
Name: count, dtype: int64

Model Accuracy: 0.8809523809523809
