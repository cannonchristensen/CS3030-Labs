import re
import time
from collections import defaultdict 
import json

# Section 1 - Follow generator function
def follow(log_file):
	log_file.seek(0,2) # Jump to the end of the file
	while True:
		line = log_file.readline()
		if not line:
			time.sleep(0.1)
			continue
		yield line # Cleanly hands off the line and pauses

# Section 2 - Setup dictionaries and regular expression
log_file = open('fakelog.log', 'r')
data = defaultdict(int) # defaultdict automatically assigns a default value to keys that do not exist
log_lines = follow(log_file)
start_time = time.time() # Starts timer at the current time
for line in log_lines:
	match = re.search(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\s-\s-\s\[[0-9]{1,2}\/[A-Z][a-z]{2}\/[0-9]{4}:[0-9]{2}:[0-9]{2}:[0-9]{2}\]\s"[A-Z]+\s(\/[\w\.-]+)\sHTTP\/1.1"\s([0-9]{3})\s[0-9]+', line) # Groups for Path and status
	if match:
		path = match.group(1)
		status = match.group(2)
		if status == "404":
			data[path] += 1
		print(dict(data)) # Dictionary dynamically grows with errors
		
# Section 3 - Timing and write to JSON
	if ((time.time() - start_time)>=60): 
		with open('404-error-counts.json', 'w') as json_file: # 'w' overwrites the file
			json.dump(data, json_file, indent=2)
		data.clear() # Clears the dictionary
		start_time = time.time() # Resets the timer