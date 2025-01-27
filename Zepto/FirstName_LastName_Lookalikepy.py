
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler


customers = pd.read_csv(r"C:/Users/sayya/Downloads/Customers.csv")
products = pd.read_csv(r"C:\Users\sayya\Downloads\Products.csv")
transactions = pd.read_csv(r"C:\Users\sayya\Downloads\Transactions.csv")

data = transactions.merge(customers, on="CustomerID").merge(products, on="ProductID")


customer_transactions = data.pivot_table(
    index='CustomerID', 
    columns='ProductName', 
    values='Quantity', 
    aggfunc='sum', 
    fill_value=0
)

scaler = StandardScaler()
scaled_data = scaler.fit_transform(customer_transactions)

similarity_matrix = cosine_similarity(scaled_data)
similarity_df = pd.DataFrame(similarity_matrix, index=customer_transactions.index, columns=customer_transactions.index)

lookalike_data = {}
for customer in customer_transactions.index[:20]:
    similar_customers = similarity_df[customer].sort_values(ascending=False)[1:4]
    lookalike_data[customer] = list(similar_customers.items())

lookalike_results = []
for cust, similar in lookalike_data.items():
    for sim_cust, score in similar:
        lookalike_results.append({'CustomerID': cust, 'SimilarCustomerID': sim_cust, 'Score': score})
lookalike_df = pd.DataFrame(lookalike_results)
lookalike_df.to_csv('FirstName_LastName_Lookalike.csv', index=False)

print("Lookalike recommendations saved to 'FirstName_LastName_Lookalike.csv'")
