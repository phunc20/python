import requests
import time
import concurrent.futures
import os

google_tw = "https://www.google.com.tw/"

t0 = time.time()

def send_request(url):
    t = time.time()
    print(f"Tx at {t-t0:.4f} by PID {os.getpid()}")
    res = requests.get(url)
    t = time.time()
    print(f"Rx at {t-t0:.4f} by PID {os.getpid()}")

urls = [google_tw]*10
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(send_request, urls)

