from pymongo import MongoClient, errors
from dotenv import load_dotenv
import os

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env.local'))

class MongoDBConnection:
    _instance = None
    _db = None
    _client = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._client = None
            cls._db = None
        return cls._instance

    def __init__(self):
        if self._client is None: 
            self.connect_to_mongo()

    def connect_to_mongo(self):
        try:
            print("Initializing MongoDB connection...")
            self._client = MongoClient(os.getenv("mongo_uri"))
            self._db = self._client["monitorizing_network"]
            print("MongoDB is connected")
        except errors.ConnectionError as e:
            print(f"Failed to connect to MongoDB: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def get_db(self):
        if not self._client:
            print("MongoDB is not connected.")
        return self._db

    def close_connection(self):
        if self._client:
            self._client.close()
            print("MongoDB connection closed.")
