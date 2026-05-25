from pathlib import Path

target_directory = '.'
files = Path(target_directory).rglob("*.tmp")

for f in files:
	print("Found junk: [" + str(f) + "]")