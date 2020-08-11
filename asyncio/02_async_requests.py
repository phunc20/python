import requests
import time
import asyncio
import os

google_tw = "https://www.google.com.tw/"
loop = asyncio.get_event_loop()

t0 = time.time()

async def send_request(url):
    t = time.time()
    print(f"Tx at {t-t0:.4f} by PID {os.getpid()}")
    #res = requests.get(url)
    res = await loop.run_in_executor(None, requests.get, url)
    t = time.time()
    PRINT(f"Rx at {t-t0:.4f} by PID {os.getpid()}")

tasks = []

for _ in range(10):
    task = loop.create_task(send_request(google_tw))
    tasks.append(task)

loop.run_until_complete(asyncio.wait(tasks))
