import pandas as pd

def quality_check():
    df = pd.read_csv("data/merged.csv")

    assert df.isnull().sum().sum() == 0

    mean = df["price"].mean()
    std = df["price"].std()

    anomalies = df[df["price"] > mean + 2*std]

    print("Anomalies:")
    print(anomalies)