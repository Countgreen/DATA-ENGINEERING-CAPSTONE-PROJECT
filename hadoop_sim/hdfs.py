import pandas as pd
import numpy as np

def simulate_hdfs():
    df = pd.read_csv("data/merged.csv")

    parts = np.array_split(df, 2)

    parts[0].to_csv("data/node1.csv", index=False)
    parts[1].to_csv("data/node2.csv", index=False)

    print("Data split into nodes (HDFS simulation)")