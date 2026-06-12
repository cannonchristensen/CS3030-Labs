import re

def parse_large_log(log_file): # generator function
	with open(log_file, 'r') as log_file:
		for line in log_file:
			yield line

data = parse_large_log("large_file.log")

for line in data:
	if "error" in line:
		print(line)

# yield is safer than read() or readlines() because yield only reads one line 
# into memory at a time. This allows it to start reading the file before loading it into
# memory. Without using a generator, it tries to load the entire file into memory.
# This could cause problems for large files because it could overload the computer's 
# memory and cause a crash.