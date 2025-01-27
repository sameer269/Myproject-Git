# Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

customers = pd.read_csv(r"C:\Users\sayya\Downloads\Customers.csv")
products = pd.read_csv(r"C:\Users\sayya\Downloads\Products.csv")
transactions = pd.read_csv(r"C:\Users\sayya\Downloads\Transactions.csv")

data = transactions.merge(customers, on="CustomerID").merge(products, on="ProductID")

top_products = data.groupby('ProductName')['TotalValue'].sum().sort_values(ascending=False).head(5)
plt.figure(figsize=(8, 5))
top_products.plot(kind='bar', color='skyblue')
plt.title('Top 5 Products by Revenue')
plt.xlabel('Product Name')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.savefig('Top_Products_Revenue.png')
plt.show()

data['TransactionDate'] = pd.to_datetime(data['TransactionDate'])
revenue_trend = data.groupby(data['TransactionDate'].dt.date)['TotalValue'].sum()
plt.figure(figsize=(10, 6))
revenue_trend.plot(color='green')
plt.title('Revenue Trend Over Time')
plt.xlabel('Transaction Date')
plt.ylabel('Total Revenue')
plt.savefig('Revenue_Trend.png')
plt.show()

top_customers = data['CustomerID'].value_counts().head(5)
plt.figure(figsize=(8, 5))
top_customers.plot(kind='bar', color='orange')
plt.title('Top 5 Customers by Transaction Count')
plt.xlabel('Customer ID')
plt.ylabel('Number of Transactions')
plt.savefig('Top_Customers_Transactions.png')
plt.show()

