import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# --- 1. DATA GENERATION (To ensure no NameError) ---
np.random.seed(42)
size = 1000
data = {
    'CustomerID': range(1001, 1001 + size),
    'SignupDate': [datetime(2024, 1, 1) + timedelta(days=np.random.randint(0, 365)) for _ in range(size)],
    'UsageHours': np.random.randint(5, 60, size),
    'MonthlyCharge': np.random.uniform(20, 150, size),
    'ContractType': np.random.choice(['Monthly', 'One-Year', 'Two-Year'], size),
    'Churn': np.random.choice([0, 1], size=size, p=[0.78, 0.22])
}
df_final = pd.DataFrame(data)

# --- 2. PREPARING DATA FOR AI ---
df_ai = df_final.copy()
# Mapping strings to numbers for the AI model
df_ai['Contract_Code'] = df_ai['ContractType'].map({'Monthly': 0, 'One-Year': 1, 'Two-Year': 2})

# Features (X) and Target (y)
X = df_ai[['UsageHours', 'MonthlyCharge', 'Contract_Code']]
y = df_ai['Churn']

# --- 3. TRAINING THE AI MODEL ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# --- 4. GENERATING AI INSIGHTS ---
accuracy = accuracy_score(y_test, model.predict(X_test))
df_final['Churn_Risk_Score'] = model.predict_proba(X)[:, 1]

print(f"--- AI Prediction Summary ---")
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("\n--- Top 5 High-Risk Customers (Identified by AI) ---")
print(df_final[['CustomerID', 'UsageHours', 'ContractType', 'Churn_Risk_Score']].sort_values(by='Churn_Risk_Score', ascending=False).head())

# Visualizing Feature Importance
importances = pd.Series(model.feature_importances_, index=X.columns)
plt.figure(figsize=(8, 4))
importances.sort_values().plot(kind='barh', color='darkblue')
plt.title('AI Insights: What Drives Customer Churn?')
plt.xlabel('Importance Score')
plt.show()
