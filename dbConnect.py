from pymongo import MongoClient
from datetime import datetime

def mongoConnect() :
    #Connect to database (localhost ou instância remota)
    client = MongoClient("mongodb://localhost:27017")
    db = client["monitorizing_network"]
    print("Mongodb is connected")
    return db

def dbCollectionDevice(db, device):
    collection = db["device"]
    device["found_In"] = datetime.now()
    collection.insert_one(device)
    print(f"Inserted {device} Successfully")

#teste
#device = {
#   "ip": "192.168.1.5",
#    "mac": "00000",
#    "host": "villa",
#    "manufacturer": "asus"
#}

#connecting db and call device
#dbCollectionDevice(device)


