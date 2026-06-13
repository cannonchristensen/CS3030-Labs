import subprocess
import re

p1 = subprocess.run('last', capture_output=True, text=True)
count = 0
logins = []

for line in p1.stdout.splitlines():
	match = re.search(r'(\w+)\s(\w+)\s+([A-z][a-z]{2}\s[A-z][a-z]{2}\s+[0-9]{1,2}\s[0-9]{2}:[0-9]{2})\s+(-\s[0-9]{2}:[0-9]{2})?\s+\(?([0-9]{2}:[0-9]{2})?\)?(.+)?', line)
	if match and count < 15:
		count = count + 1
		user = match.group(1)
		terminal = match.group(2)
		if match.group(4):
			date = match.group(3) + " " + match.group(4)
		else:
			date = match.group(3)
		if match.group(5):
			duration = match.group(5)
		elif match.group(6):
			duration = match.group(6)
		entry = {
			"user": user,
			"terminal": terminal,
			"date": date,
			"duration": duration
		}
		logins.append(entry)
			
header = f"| {'User':<20}{'Terminal':<12}{'Date':<30}{'Duration':<15} |"
print("+" + "-" * (len(header)-2) + "+")
print(header)	
print("+" + "-" * (len(header)-2) + "+")
for login in logins:
	print(f"| {login['user']:<20}{login['terminal']:<12}{login['date']:<30}{login['duration']:<15} | ")
print("+" + "-" * (len(header)-2) + "+")