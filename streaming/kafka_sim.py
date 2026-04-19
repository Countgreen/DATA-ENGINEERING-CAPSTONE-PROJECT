import time

def producer():
    for i in range(5):
        print("Producing:", i)
        yield i
        time.sleep(1)

def consumer():
    for data in producer():
        print("Consuming:", data)

if __name__ == "__main__":
    consumer()