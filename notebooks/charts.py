import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/cleaned_superstore.csv")

region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8,5))
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.ylabel("Sales")
plt.tight_layout()

plt.savefig("../dashboard/sales_by_region.png")

plt.show()