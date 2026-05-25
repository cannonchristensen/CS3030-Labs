# Section 2

## Security Report
Developers should never use `shell=True` with unvalidated user input because it could allow the user to inject malicious commands. The user can type a semicolon (;) to end the current command and enter their own command. This can be prevented by passing arguments as a list, because that method defines the command first and then the user can only pass arguments to that command.