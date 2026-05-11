# Section 1

## The "Sentinel" Script
The Sentinel script is used to check if a exists. It requires one argument, which is the absolute or relative directory path you want to check. It then outputs a success or an error depending on whether the directory exists.

## 3 Useful Shell Commands
### mkdir
The `mkdir` command is useful because it allows you to quickly create directories. It is possible to include several directory names to create, and the command will create them all at once.

### ls
The `ls` command is useful for viewing the contents of a directory. It is very helpful to understand where you are and to view what files are in the directory. The -l option is useful to see detailed information about file contents, and the -a option is useful to show hidden files, including dot files.

### cp
The `cp` command is useful for quickly copying files. It allows you to specify multiple items to copy into a directory, with the last name included in the command being the directory to copy into.

## How to Configure .venv and install dependencies
1. Navigate to your workspace directory.
2. To create a virtual environment inside the directory, use the command `python3 -m venv .venv`. This keeps your project's packages separate from the system.
3. Activate your virtual environment with the command `source .venv/bin/activate`.
4. Your terminal should now include `(.venv)` at the beginning of each line, indicating that you are working within the virtual environment.
5. Install required dependencies with the command `pip install -r task6/requirements.txt` (from within the section1 directory).