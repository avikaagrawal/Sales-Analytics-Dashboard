import pandas as pd

df = pd.read_csv(
    "../data/cleaned_superstore.csv"
)

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
avg_order_value = total_sales / total_orders
profit_margin = (total_profit / total_sales) * 100

print("\n===== KPI SUMMARY =====")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Average Order Value: ${avg_order_value:,.2f}")
print(f"Profit Margin: {profit_margin:.2f}%")