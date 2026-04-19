from ingestion.ingest import ingest

def run_elt():
    df = ingest()
    df.to_csv("data/elt_loaded.csv", index=False)