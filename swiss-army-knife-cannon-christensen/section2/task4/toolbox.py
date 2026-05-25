import argparse
from pathlib import Path

parser = argparse.ArgumentParser(
	prog="Toolbox", 
	description="Search a specified directory and its subdirectories for files with a specified extension. This tool will print the relative paths of matching files.",
	epilog="Example: toolbox --path pathToSearch --ext txt")
parser.add_argument("--path", required=True, help="Specify the directory to search within")
parser.add_argument("--ext", required=True, help="Specify the file extension to search for")
args = parser.parse_args()

target_directory = args.path
files = Path(target_directory).rglob("*." + args.ext)

for f in files:
	print("Found junk: [" + str(f) + "]")