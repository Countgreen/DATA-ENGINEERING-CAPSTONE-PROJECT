import pandas as pd
import time

def stream_data():
    df = pd.read_csv("data/real_data.csv")

    records = []

    for i in range(10):
        price = df.iloc[i]["CLOSE"]

        print("Streaming:", price)

        records.append({"price": price})

        time.sleep(1)

    df_stream = pd.DataFrame(records)
    df_stream.to_csv("data/stream_data.csv", index=False)

if __name__ == "__main__":
    stream_data()