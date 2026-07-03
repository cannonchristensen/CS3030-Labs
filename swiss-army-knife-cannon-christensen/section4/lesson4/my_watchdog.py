from datetime import datetime
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watch: # Observer class
	watchDirectory = "." #Directory to watch
	
	def __init__(self): # Constructor. Runs when you create an object from a class.
		self.observer = Observer() # Creates an Observer object when a Watch object is made. Self is object you're currently working with (like this in other languages).
		
	def run(self):
		event_handler = Handler() # Creates Handler object
		self.observer.schedule(event_handler, self.watchDirectory, recursive = True) # Tells that event_handler handles events, self.watchDirectory (".") should e watched, also watch recursively.
		self.observer.start() # Starts the observer
		try:
			while True:
				time.sleep(5)
		except:
			self.observer.stop()
			print("Observer Stopped")
				
		self.observer.join() # Wait until the observer is done before the program exits
	
	
class Handler(FileSystemEventHandler): # Event handler notified when something happens to file system

	def on_modified(self, event): # Executes when a file is modified
		
		if event.is_directory:
			return None
		
		current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		print(f"[{current_time}] - File modified: % s." % event.src_path)
		
if __name__ == '__main__': # Only run when file is executed directly (Allows importing).
	watch = Watch()
	watch.run()