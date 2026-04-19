import shutil

def upload():
    shutil.copy("data/merged.csv", "cloud/merged.csv")
    print("Uploaded to cloud (simulated)")