import sys, os, certifi

ca = certifi.where()
from dotenv import load_dotenv

load_dotenv()
mongo_db_url = os.getenv("MONGODB_URL")
print(mongo_db_url)

import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.pipeline.training_pipeline import TrainingPipeline