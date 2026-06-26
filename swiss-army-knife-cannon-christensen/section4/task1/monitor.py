import psutil
from colorama import Fore
from datetime import datetime

cpu_percent = psutil.cpu_percent(1)
available_ram = round(psutil.virtual_memory().available / (1024**3), 2)
disk_usage = psutil.disk_usage('/').percent

print(f"""Timestamp: {datetime.now().isoformat()}
CPU Usage: {cpu_percent}%
Available RAM: {available_ram} GB
Disk Usage Percentage: {disk_usage}%
""")

if cpu_percent > 80:
	print(Fore.RED + "WARNING: CPU Usage Above 80%")
if available_ram < 1.0:
	print(Fore.RED + "WARNING: Less than 1 GB RAM available")
if disk_usage > 90:
	print(Fore.RED + "WARNING: Disk Usage Exceeds 90%")
