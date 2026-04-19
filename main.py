from ingestion.ingest import ingest
from processing.transform import process
from quality.quality import quality_check

def run():
    df = ingest()
    df = process(df)

    df.to_csv("data/final.csv", index=False)

    quality_check()

    print("Pipeline Completed Successfully")

if __name__ == "__main__":
    run()