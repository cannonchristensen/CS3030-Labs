# A malicious attacker could use the unsafe function to pass malicious input such as 
# "; cat /etc/passwd". This is possible because the unsafe function accepts the entire 
# input as shell input, so anything the user types will be passed into the shell. 
# While the code contains the echo command, the user could type a semicolon (;)  
# to end that command and pass a new command into the shell. The safe function prevents 
# this by providing the command first, and then the input for that command, so the user 
# can't end the command and start a new one.


import subprocess

def unsafe_run(user_input):
	subprocess.run(f"echo {user_input}", shell=True)

def safe_run(user_input):
	subprocess.run(["echo", user_input])
	
print("Enter input:")
new_input = input()
unsafe_run(new_input)
safe_run(new_input)