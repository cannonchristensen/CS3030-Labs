import time
import random
from datetime import datetime

# Configuration
LOG_FILE = "mock_access.log"
DELAY_RANGE = (0.5, 2.0)  # Seconds to wait between log entries

# Mock data pools
IP_ADDRESSES = ["192.168.1.50", "10.0.0.12", "172.16.0.5", "192.168.1.101", "10.0.0.55"]
REQUEST_METHODS = ["GET", "POST", "PUT", "DELETE"]
RESOURCES = [
    "/index.html", "/api/v1/login", "/images/logo.png", "/css/styles.css",
    "/api/v1/users", "/checkout", "/products/item-452", "/admin/dashboard",
    "/hidden-backup.tar.gz", "/wp-login.php" # Some unusual paths for fun regex filtering
]
STATUS_CODES = [200, 200, 200, 200, 301, 404, 404, 500] # Weighted toward 200s
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Python-urllib/3.10",
    "curl/7.68.0"
]

def generate_log_line():
    """Generates a single fake Nginx/Apache style log line."""
    ip = random.choice(IP_ADDRESSES)
    timestamp = datetime.now().strftime("%d/%b/%Y:%H:%M:%S +0000")
    method = random.choice(REQUEST_METHODS)
    resource = random.choice(RESOURCES)
    
    # Give 404s higher likelihood on specific sensitive paths
    if resource in ["/admin/dashboard", "/wp-login.php"]:
        status = random.choice([404, 500, 200])
    else:
        status = random.choice(STATUS_CODES)
        
    bytes_sent = random.randint(150, 5000) if status == 200 else random.randint(20, 300)
    user_agent = random.choice(USER_AGENTS)
    
    return f'{ip} - - [{timestamp}] "{method} {resource} HTTP/1.1" {status} {bytes_sent} "{user_agent}"\n'

def main():
    print(f"ðŸš€ Starting mock log generator. Writing to '{LOG_FILE}'...")
    print("Press Ctrl+C to stop.")
    
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            while True:
                log_line = generate_log_line()
                f.write(log_line)
                f.flush()  # Force write to disk instantly so 'tail' can see it
                
                # Optional: print to console so you can see it working
                print(log_line.strip())
                
                # Sleep for a random interval to simulate real traffic variance
                time.sleep(random.uniform(*DELAY_RANGE))
    except KeyboardInterrupt:
        print("\nStopping log generator. Goodbye!")

if __name__ == "__main__":
    main()