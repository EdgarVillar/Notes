import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

print("--- Step 1: Loading Data ---")
iris = load_iris()
X, y = iris.data, iris.target

print("--- Step 2: Training Random Forest Model ---")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

print("--- Step 3: Serializing (Saving) the Model ---")
# joblib is highly optimized for saving scikit-learn models
joblib.dump(model, "model.pkl")

print("✅ Model saved successfully as 'model.pkl'! It is now ready for deployment.")
