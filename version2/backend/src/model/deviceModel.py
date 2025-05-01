from db_connection import MongoDBConnection
from datetime import datetime

class DeviceModel:
    def __init__(self, ip, mac, host, status, manufacturer, found_in=None):
        self.db = MongoDBConnection().get_db()
        self.collection = self.db["devices"]
        self.ip = ip
        self.mac = mac
        self.host = host
        self.status = status
        self.manufacturer = manufacturer
        self.found_in = found_in

    def device_exists(self):
        return self.collection.find_one({"mac": self.mac}) is not None
    
    def save_device(self):
        if self.device_exists():
            print(f"Device already exists: {self.mac}")
        else:
            try:
                self.collection.insert_one({
                    "ip": self.ip,
                    "mac": self.mac,
                    "host": self.host,
                    "status": self.status,
                    "manufacturer": self.manufacturer,
                    "found_in": self.found_in
                })
                print(f"Inserted device {self.mac} successfully.")
            except Exception as e:
                print(f"Failed to insert device {self.mac}: {e}")
    
    def __repr__(self):
        return f"Device(ip={self.ip}, mac={self.mac}, host={self.host}, status={self.status}, manufacturer={self.manufacturer}, found_in={self.found_in})"
    
    @classmethod
    def get_all_devices(cls):
        db = MongoDBConnection().get_db()
        collection = db["devices"]

        return list(collection.find())