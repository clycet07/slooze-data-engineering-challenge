import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../data/processed/products.csv")

print(df.head())

print("\nSummary Statistics:")
print(df.describe())

print("\nTop locations:")
print(df["location"].value_counts().head(10))

plt.figure()
df["location"].value_counts().head(10).plot(kind="bar")
plt.title("Top Supplier Locations")
plt.show()

plt.figure()
sns.histplot(df["price"].dropna())
plt.title("Price Distribution")
plt.show()
