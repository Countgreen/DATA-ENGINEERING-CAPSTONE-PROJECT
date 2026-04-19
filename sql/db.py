import sqlite3
import pandas as pd

def load_db():
    conn = sqlite3.connect("db.sqlite")
    df = pd.read_csv("data/merged.csv")
    df.to_sql("crypto", conn, if_exists="replace", index=False)
    return conn