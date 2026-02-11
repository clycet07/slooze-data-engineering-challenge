import pandas as pd
import json

def transform():

    with open("../data/raw/products.json") as f:
        data = json.load(f)

    df = pd.DataFrame(data)

    df["price"] = df["price"].str.replace("₹","", regex=False)
    df["price"] = df["price"].str.replace(",","", regex=False)

    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    df = df.drop_duplicates()

    df.to_csv("../data/processed/products.csv", index=False)

    print("ETL completed")


if __name__ == "__main__":
    transform()
