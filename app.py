import sys, os, certifi

ca = certifi.where()
from dotenv import load_dotenv

load_dotenv()
mongo_db_url = os.getenv("MONGODB_URL")
print(mongo_db_url)