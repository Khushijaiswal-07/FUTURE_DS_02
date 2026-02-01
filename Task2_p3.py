import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# --- 1. PROFESSIONAL DATASET GENERATION ---
# Specifically designed to meet Task 2 criteria for subscription analysis
np.random.seed(42)
sample_size = 1000
data = {
    'CustomerID': range(1001, 1001 + sample_size),
    'SubscriptionDate': [datetime(2024, 1, 1) + timedelta(days=np.random.randint(0, 365)) for _ in range(sample_size)],
    'UsageHours_PerMonth': np.random.randint(5, 55, sample_size),
    'ContractType': np.random.choice(['Monthly', 'One-Year', 'Two-Year'], sample_size),
    'Churn': np.random.choice([0, 1], size=sample_size, p=[0.78, 0.22])  # 22% Simulated Churn Rate
}

df_task2 = pd.DataFrame(data)

# --- 2. KPI CALCULATION ---
total_customers = len(df_task2)
churned_count = df_task2['Churn'].sum()
churn_rate = (churned_count / total_customers) * 100

print(f"--- Task 2: Executive Summary ---")
print(f"Total Unique Customers Analyzed: {total_customers}")
print(f"Overall Churn Rate: {churn_rate:.2f}% \n")

# --- 3. PROFESSIONAL VISUALIZATION ---
plt.style.use('ggplot')
fig, ax = plt.subplots(1, 2, figsize=(16, 6))

# A. Retention Analysis by Contract Type
sns.countplot(x='ContractType', hue='Churn', data=df_task2, ax=ax[0], palette='viridis')
ax[0].set_title('Churn Analysis by Contract Category')
ax[0].set_ylabel('Customer Count')

# B. Usage Impact Analysis
sns.boxplot(x='Churn', y='UsageHours_PerMonth', data=df_task2, hue='Churn', palette='magma', ax=ax[1], legend=False)
ax[1].set_title('Impact of Service Usage on Retention')
ax[1].set_xticks(ax[1].get_xticks())
ax[1].set_xticklabels(['Retained', 'Churned'])

plt.tight_layout()
plt.show()
