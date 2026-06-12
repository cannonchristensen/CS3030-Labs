import re

log_file = open('sample.log')
data = log_file.readlines()
ips = []
timestamps = []

for line in data:
	timestamp_regex = re.search(r'\[[0-9]{4}(-[0-9]{2}){2}\ [0-9]{2}:[0-9]{2}\]', line)
	ip_regex = re.search(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', line)
	if timestamp_regex:
		timestamps.append(timestamp_regex.group())
	if ip_regex:
		ips.append(ip_regex.group())
	
print("Timestamps:")
for timestamp in timestamps:
	print(timestamp)
print("\n IP Addresses:")
for ip in ips:
	print(ip)
