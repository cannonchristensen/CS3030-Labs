import os

directory = '.'
name_string = "Hawaii_Trip_"

count = 1;

for name in os.listdir(directory):
	if not name.startswith('.') and name.endswith('.jpg'):
		old_file = os.path.join(directory, name)
		new_file = os.path.join(directory, name_string + str(count).zfill(2) + ".jpg")
	
		os.rename(old_file, new_file)
		print(f"Renamed: {name} to {name_string}{str(count).zfill(2)}.jpg")
	
		count += 1