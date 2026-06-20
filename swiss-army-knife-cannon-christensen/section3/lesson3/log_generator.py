from datetime import datetime
import time
import random

# Create lists of possible values
ip_addresses = ["192.168.2.50", "10.0.0.15", "10.0.0.2", "192.168.201.50", "192.168.2.41"]
http_methods = [("\"GET /index.html HTTP/1.1\""), ("\"POST /login HTTP/1.1\""), "\"GET /secret-admin HTTP/1.1\""]
status_codes = ["200", "200", "200", "404", "404", "500"]
size = ["232", "1024", "4345", "0"]

while True:
	now = datetime.now()
	date_string = now.strftime("%d/%b/%Y:%H:%M:%S") # Format current time for log
	new_line = random.choice(ip_addresses) + " - - [" + date_string + 	"] " + random.choice(http_methods) + " " + random.choice(status_codes) + " " + random.choice(size) # Build log string with random values
	print(new_line)
	# Append line to the log file
	with open ("fakelog.log", "a") as file:
		file.write(new_line + "\n")
	time.sleep(random.uniform(1,5)) # Wait 1-5 seconds