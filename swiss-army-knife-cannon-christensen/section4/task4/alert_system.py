import requests
import os
import psutil
from dotenv import load_dotenv

load_dotenv()

webhook = os.getenv("WEBHOOK")

disk_usage = psutil.disk_usage('/System/Volumes/Data').percent

url_list = ["https://github.com", "https://www.apple.com", "https://musicians.int"]

def send_alert(message):
    requests.post(webhook, json={"content": message})

if disk_usage > 90:
    send_alert("WARNING: Disk Usage Exceeds 90%")

for url in url_list:
    try:
        response = requests.get(url)
        if response.status_code != 200:
            send_alert(f"{url}: SITE DOWN")
    except requests.exceptions.RequestException:
        send_alert(f"{url}: SITE DOWN")
