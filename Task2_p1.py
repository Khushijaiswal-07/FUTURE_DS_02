import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# --- 1. DATASET PREPARATION ---
# Generating specialized subscription data to meet Task 2 requirements
np.random.seed(42)
sample_size = 1000
data = {
    'CustomerID': range(1001, 1001 + sample_size),
    'SubscriptionDate': [datetime(2024, 1, 1) + timedelta(days=np.random.randint(0, 365)) for _ in range(sample_size)],
    'UsageHours_PerMonth': np.random.randint(5, 50, sample_size),
    'MonthlyCharge': np.random.uniform(15, 120, sample_size),
    'ContractType': np.random.choice(['Monthly', 'One-Year', 'Two-Year'], sample_size),
    'Churn': np.random.choice([0, 1], size=sample_size, p=[0.78, 0.22])  # 22% Simulated Churn Rate
}

df = pd.DataFrame(data)

# --- 2. CALCULATING KPI METRICS ---
total_users = len(df)
churned_users = df['Churn'].sum()
retention_rate = ((total_users - churned_users) / total_users) * 100
churn_rate = (churned_users / total_users) * 100

print(f"--- Executive Summary ---")
print(f"Total Unique Customers: {total_users}")
print(f"Churned Customers: {churned_users}")
print(f"Retention Rate: {retention_rate:.2f}%")
print(f"Churn Rate: {churn_rate:.2f}% \n")

# --- 3. DATA VISUALIZATION ---
plt.style.use('ggplot')
fig, ax = plt.subplots(1, 2, figsize=(15, 6))

# A. Churn Distribution by Contract Type
sns.countplot(x='ContractType', hue='Churn', data=df, ax=ax[0], palette='viridis')
ax[0].set_title('Churn Analysis by Contract Type')
ax[0].set_ylabel('Customer Count')

# B. Usage Impact on Retention
sns.boxplot(x='Churn', y='UsageHours_PerMonth', data=df, hue='Churn', palette='Set2', ax=ax[1], legend=False)
ax[1].set_title('Impact of Service Usage on Retention')
ax[1].set_xticks([0, 1])  
ax[1].set_xticklabels(['Retained', 'Churned'])

plt.tight_layout()
plt.show()


