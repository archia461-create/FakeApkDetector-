import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_csv("dataset.csv")

# Encode labels: fake=1, safe=0
df['label'] = df['label'].map({'fake': 1, 'safe': 0})

# Features (exclude app_name & package_name)
X = df[['has_bank_keyword', 'permissions_count', 'file_size_kb',
        'has_sms_permission', 'has_camera_permission']]
y = df['label']

# Split data (optional, for evaluation)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Optional: Evaluate accuracy
accuracy = model.score(X_test, y_test)
print(f"Model trained! Accuracy on test set: {accuracy*100:.2f}%")

# Save trained model
joblib.dump(model, "model.pkl")
print("Trained model saved as model.pkl")
