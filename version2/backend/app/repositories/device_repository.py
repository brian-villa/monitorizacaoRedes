
class DeviceRepository:
    def __init__(self, db):
        self.collection = db["devices"]

    def insert(self, device:dict):
        if not self.find_by_mac(device["mac"]):
            self.collection.insert_one(device)
            print(f"Device: {device['mac']}inserted.")
        else:
            print(f"Device{device["mac"]} already exist.")
    
    def get_by_mac(self, mac: str):
        return self.collection.find_one({"mac": mac})
    
    def get_all(self):
        return list(self.collection.find())


        