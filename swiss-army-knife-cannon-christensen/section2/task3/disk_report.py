import subprocess

p1 = subprocess.run(['df', '-h'], capture_output=True, text=True)

for line in p1.stdout.splitlines():
	columns = line.split()
	if columns and columns[-1] == "/System/Volumes/Data":
		print(line)