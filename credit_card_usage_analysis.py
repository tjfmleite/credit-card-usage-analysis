import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('credit_card_usage.csv')

# Display the first few rows of the dataset
print("Dataset Overview:")
print(data.head())

# 1. Analyze Spending Score by Region
spending_by_region = data.groupby('Region')['SpendingScore'].mean()
print("\nAverage Spending Score by Region:")
print(spending_by_region)

# Visualize Spending Score by Region
plt.figure(figsize=(8, 5))
spending_by_region.plot(kind='bar', color='blue', title='Average Spending Score by Region')
plt.ylabel('Average Spending Score')
plt.xlabel('Region')
plt.tight_layout()
plt.savefig('spending_by_region.png')
plt.show()

# 2. Analyze Transactions by Card Type
transactions_by_card = data.groupby('CardType')['Transactions'].mean()
print("\nAverage Transactions by Card Type:")
print(transactions_by_card)

# Visualize Transactions by Card Type
plt.figure(figsize=(8, 5))
transactions_by_card.plot(kind='bar', color='green', title='Average Transactions by Card Type')
plt.ylabel('Average Transactions')
plt.xlabel('Card Type')
plt.tight_layout()
plt.savefig('transactions_by_card.png')
plt.show()

# 3. Correlation Analysis
correlation_matrix = data[['Age', 'AnnualIncome', 'SpendingScore', 'Transactions']].corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

# Heatmap for Correlation Matrix
import seaborn as sns
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix Heatmap')
plt.tight_layout()
plt.savefig('correlation_heatmap.png')
plt.show()

# 4. Identify High-Spending Customers
high_spenders = data[data['SpendingScore'] > 75]
print("\nHigh-Spending Customers:")
print(high_spenders)

# Save High-Spending Customers to a CSV
high_spenders.to_csv('high_spending_customers.csv', index=False)
print("High-spending customers saved to 'high_spending_customers.csv'.")
