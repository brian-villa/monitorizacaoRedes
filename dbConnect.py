from pymongo import MongoClient
from datetime import datetime

def mongoConnect():
    # Connect to database (localhost or remote instance)
    client = MongoClient("mongodb://localhost:27017")
    db = client["monitorizing_network"]
    print("Mongodb is connected")
    return db

def dbCollectionDevice(db, device):
    collection = db["device"]
    # Check if the device already exists by MAC address
    if collection.find_one({"mac": device["mac"]}):
        print(f"Device already exists: {device['mac']}")
        return
    # Insert the device if it doesn't exist
    collection.insert_one(device)
    print(f"Inserted {device} Successfully")
