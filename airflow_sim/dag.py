import schedule
import time

def job():
    try:
        print("Pipeline running...")
    except:
        print("Retrying...")

schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)