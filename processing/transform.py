import pandas as pd

def process(df):
    df["rolling_avg"] = df["price"].rolling(2).mean()
    df["normalized"] = df["price"] / df["price"].max()

    # simulate large data
    df = pd.concat([df]*1000)
    df = df.astype("float32")

    return df