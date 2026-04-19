from ingestion.ingest import ingest
from processing.transform import process

def run_etl():
    df = ingest()
    df = process(df)
    df.to_csv("data/etl_output.csv", index=False)