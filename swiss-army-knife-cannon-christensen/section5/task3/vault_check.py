import os
from dotenv import load_dotenv

load_dotenv()

secret_key = os.getenv("SUPER_SECRET_KEY")

print("Accessing system with key: " + '*' * (len(secret_key)-3) + secret_key[-3:])