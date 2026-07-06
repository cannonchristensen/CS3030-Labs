try:
	with open("config.txt", 'r') as file:
		data = file.read()
		data = data.replace("theme=dark", "theme=light")
	
	with open("config.txt", 'w') as file:
		file.write(data)
	
except FileNotFoundError:
	print("Error: configuration file missing.")
except PermissionError:
	print("Error: user does not have permission to access the file.")
except Exception:
	print("Error.")
finally:
	print("Operation Attempted")