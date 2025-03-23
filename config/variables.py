import os

from dotenv import load_dotenv

load_dotenv()

DB_USERNAME = os.getenv("MONGO_ROOT_USERNAME")
DB_PASSWORD = os.getenv("MONGO_ROOT_PASSWORD")
DB_HOST = os.getenv("MONGO_ROOT_HOST")
DB_PORT = os.getenv("MONGO_ROOT_PORT")
DB_NAME = os.getenv("MONGO_DB_NAME")
DB_ENTRIES = int(os.getenv("MONGO_DB_ENTRIES", 1000))
