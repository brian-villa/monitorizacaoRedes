from pymongo import MongoClient, errors
from dotenv import load_dotenv
import os

from pathlib import Path
dotenv_path = Path(__file__).resolve().parents[2] / "env" / ".env.local"
load_dotenv(dotenv_path)


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

            mongo_uri = os.getenv('mongodb')

            if not mongo_uri:
                print(f"ERROR: mongo_uri is not defined in the .env.local file")
                return
     
            self._client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)

            self._client.server_info()
          
            self._db = self._client["monitorizing_network"]
            print("MongoDB connected successfully!")
            
        except errors.ServerSelectionTimeoutError:
            print("ERROR: Could not connect to the MongoDB server. Please ensure the server is running.")
            self._client = None
        except errors.ConfigurationError as e:
            print(f"MongoDB configuration ERROR: {e}")
            self._client = None
        except errors.ConnectionFailure as e:
            print(f"MongoDB connection ERROR: {e}")
            self._client = None
        except Exception as e:
            print(f"Unexpected ERROR: {e}")
            self._client = None

    def get_db(self):
        if not self._client:
            print("MongoDB is not connected.")
            return None
        return self._db

    def close_connection(self):
        if self._client:
            self._client.close()
            print("Connection to MongoDB closed.")