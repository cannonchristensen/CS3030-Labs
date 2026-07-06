# Final Cleanup

## Security and Robustness Checklist
* **Enforce virtual environments**: Store secrets in an .env file in the root of the project, and load them with the `load_dotenv` module.
* **Configure .gitignore**: Ensure that .env and other sensitive or temporary files are added to the `.gitignore` file so they do not become publicly available.
* **Mask environment variables**: If used in scripts, environment variables should be masked. The full output should never be printed to the console or otherwise available.
* **Include exceptions**: Wrap code in a `try` block with exceptions enumerated so that scripts fail gracefully with readable error messages.
* **Order exception catching**: Catch specific exceptions first, and only use `Exception` as a fallback once all other exceptions have been listed. 
* **Use logging instead of print statements**: Use the `logging` module instead of print statements to save log information. This is useful for saving to a file or retaining information.
* **Repository cleanup**: Delete unused files and remove from version control as needed, and ensure scripts run without errors.

## Technical Reflection
I thought section 4 was the most challenging, because it introduced a lot of new and unfamiliar concepts relating to system administration. For the heartbeat script, I researched how to use psutil and crontab. With the heartbeat log, I was getting some messy line spacing between print statements, so I switched to a single multiline print statement that will run once during the script. For the web health checker, because a fake URL will not return any status code, I had to add the RequestException and then print an error when the exception occurs. For the systemd daemon, I had to figure out exactly what to put into the service file, and then it still had an error. In order to get the script to run as a daemon, I had to modify it to run continuously and sleep for 60 seconds. For the regular expressions in section 3, a lot of trial and error was required to get the regular expressions to work properly.