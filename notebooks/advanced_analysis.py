import pandas as pd

df = pd.read_csv("../data/cleaned_superstore.csv")

# Top 10 Products
top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTOP 10 PRODUCTS")
print(top_products)

# Top 10 Customers
top_customers = (
    df.groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTOP 10 CUSTOMERS")
print(top_customers)
# Most Profitable Products

top_profit_products = (
    df.groupby("Product Name")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTOP 10 PROFITABLE PRODUCTS")
print(top_profit_products)