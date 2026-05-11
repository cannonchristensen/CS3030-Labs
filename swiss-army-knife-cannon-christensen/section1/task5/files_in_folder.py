import os 
# Get a list of visible files/folders in the current directory ('.')
files = [f for f in os.listdir('.') if not f.startswith('.')]
print(f"I found {len(files)} files in this directory:")
for f in files:
    print(f"- {f}")