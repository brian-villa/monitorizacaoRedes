from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env.local'))

def mongoConnect():
    # Connect to database (localhost or remote instance)
    client = MongoClient(os.getenv("mongo_uri")) #mudar url para a url do teu DB
    db = client["monitorizing_network"]
    print("Mongodb is connected")
    return db

def dbCollectionDevice(db, device):
    collection = db["devices"]
    # Check if the device already exists by MAC address
    if collection.find_one({"mac": device["mac"]}):
        print(f"Device already exists: {device['mac']}")
        return
    else:
        # Insert the device if it doesn't exist
        collection.insert_one(device)
        print(f"Inserted {device} Successfully\n")
