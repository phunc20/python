import requests
import time
import os

google_tw = "https://www.google.com.tw/"

t0 = time.time()

def send_request(url):
    t = time.time()
    #print(f"Send request at    {t-t0:.4f}")
    print(f"Tx at {t-t0:.4f} by PID {os.getpid()}")
    res = requests.get(url)
    t = time.time()
    #print(f"Receive request at {t-t0:.4f}")
    print(f"Rx at {t-t0:.4f} by PID {os.getpid()}")


for _ in range(10):
    send_request(google_tw)
