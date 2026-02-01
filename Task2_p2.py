import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# --- 1. DATASET GENERATION ---
# Creating a professional subscription dataset specifically for Task 2
np.random.seed(42)
sample_size = 1000
data = {
    'CustomerID': range(101, 101 + sample_size),
    'SignupDate': [datetime(2024, 1, 1) + timedelta(days=np.random.randint(0, 365)) for _ in range(sample_size)],
    'UsageHours': np.random.randint(2, 60, sample_size),
    'ContractType': np.random.choice(['Monthly', 'One-Year', 'Two-Year'], sample_size),
    'Churn': np.random.choice([0, 1], size=sample_size, p=[0.75, 0.25])  # 25% Churn Rate
}

df = pd.DataFrame(data)

# --- 2. CALCULATING KPI METRICS ---
total_customers = len(df)
churned_count = df['Churn'].sum()
retention_rate = ((total_customers - churned_count) / total_customers) * 100
churn_rate = (churned_count / total_customers) * 100

print(f"--- Executive Summary ---")
print(f"Total Unique Customers: {total_customers}")
print(f"Retained Customers: {total_customers - churned_count}")
print(f"Retention Rate: {retention_rate:.2f}%")
print(f"Churn Rate: {churn_rate:.2f}% \n")

# --- 3. DATA VISUALIZATION ---
plt.style.use('ggplot')
fig, ax = plt.subplots(1, 2, figsize=(16, 6))

# A. Retention by Contract Type
sns.countplot(x='ContractType', hue='Churn', data=df, ax=ax[0], palette='viridis')
ax[0].set_title('Customer Retention vs Churn by Contract')
ax[0].set_ylabel('Customer Count')

# B. Usage Impact Analysis
sns.boxplot(x='Churn', y='UsageHours', data=df, hue='Churn', palette='magma', ax=ax[1], legend=False)
ax[1].set_title('Impact of Service Usage on Retention')
ax[1].set_xticks(ax[1].get_xticks())
ax[1].set_xticklabels(['Active', 'Churned'])

plt.tight_layout()
plt.show()
