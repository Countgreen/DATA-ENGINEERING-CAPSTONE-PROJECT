import shutil
import time

def version_data():
    timestamp = int(time.time())
    shutil.copy("data/merged.csv", f"lakehouse/data_{timestamp}.csv")
    print("Version created")