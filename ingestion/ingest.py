import pandas as pd

def ingest():
    df1 = pd.read_csv("data/raw1.csv")
    df2 = pd.read_csv("data/raw2.csv")

    df = pd.concat([df1, df2])
    df.fillna(0, inplace=True)

    df.to_csv("data/merged.csv", index=False)
    return df