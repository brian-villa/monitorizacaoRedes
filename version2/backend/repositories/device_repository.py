class DeviceRepository:
   
    def __init__(self, db_connection):   
        db = db_connection.get_db() if db_connection else None

        if db is None:
            print("Database connection not available.")
            self.collection = None
        else:
            self.collection = db["devices"]
            print("Success!!")

    def insert(self, device: dict):
        if self.collection is None:
            print("Database not connected")
            return False

        try:
            result = self.collection.update_one(
                {"mac": device["mac"]},
                {"$setOnInsert": device},
                upsert=True
            )
            return result.upserted_id is not None
        except Exception as e:
            print(f"Database error: {e}")
            return False

    def find_by_mac(self, mac: str):
        if self.collection is None:
            print(f"WARNING: Could not search for device {mac} - database not connected.")
            return None

        try:
            return self.collection.find_one({"mac": mac})
        except Exception as e:
            print(f"Error searching for device by MAC: {e}")
            return None

    def get_by_mac(self, mac: str):
        return self.find_by_mac(mac)

    def get_all(self):
        if self.collection is None:
            print("WARNING: Could not list devices - database not connected.")
            return []

        try:
            return list(self.collection.find())
        except Exception as e:
            print(f"Error listing all devices: {e}")
            return []