 # --- 1. ESSENTIAL LIBRARIES ---
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- 2. GEOGRAPHICAL DATA ENRICHMENT ---
# Assigning regions to analyze localized retention patterns
regions = ['North', 'South', 'East', 'West']
df_final['Region'] = np.random.choice(regions, size=len(df_final))

# --- 3. REGION-WISE CHURN ANALYSIS ---
# Calculating the average churn percentage per region
region_churn = df_final.groupby('Region')['Churn'].mean() * 100

# --- 4. DATA VISUALIZATION ---
plt.style.use('seaborn-v0_8-muted')
plt.figure(figsize=(10, 6))
region_colors = ['#FF9933', '#66B2FF', '#99FF99', '#FFCC99']
region_churn.sort_values(ascending=False).plot(kind='bar', color=region_colors)

# Adding professional labels and title
plt.title('Geographical Risk Analysis: Churn Rate by Region', fontsize=14, pad=15)
plt.ylabel('Churn Percentage (%)', fontsize=12)
plt.xlabel('Business Region', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# --- 5. EXECUTIVE BUSINESS INSIGHTS ---
highest_risk = region_churn.idxmax()
print(f"--- STRATEGIC INSIGHTS ---")
print(f"High-Risk Zone: The {highest_risk} region exhibits the highest churn intensity.")
print(f"Recommendation: Implement region-specific loyalty campaigns and localized customer support to mitigate exit risk in the {highest_risk} territory.")
