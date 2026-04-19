import pandas as pd
import numpy as np

def spark_simulation():
    df = pd.read_csv("data/merged.csv")

    partitions = np.array_split(df, 4)
    cached = partitions[0]

    result = pd.concat(partitions).groupby("price").mean()

    print("Spark Simulation Result:")
    print(result)