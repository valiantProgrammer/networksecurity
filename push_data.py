import os 
import sys
from dotenv import load_dotenv

MONGODB_URL=os.getenv("MONGODB_URL")
print(MONGODB_URL)