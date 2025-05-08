from datetime import datetime

class DeviceRepository:
    def __init__(self, db_connection):
        db = db_connection.get_db() if db_connection else None
        if db is None:
            print("Database connection not available.")
            self.collection = None
        else:
            self.collection = db["devices"]
            print(f"Success creating collection of devices!!")

    def insert(self, device: dict):
        if self.collection is None:
            print("Database not connected")
            return False
            
        if "status" not in device:
            device["status"] = "unknown"
            
        try:
            result = self.collection.insert_one(device)
            return result.inserted_id is not None
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
            
    def find_by_status(self, status: str):
        """Find all devices with a specific status"""
        if self.collection is None:
            print(f"WARNING: Could not search for devices with status {status} - database not connected.")
            return []
        try:
            return list(self.collection.find({"status": status}))
        except Exception as e:
            print(f"Error searching for devices by status: {e}")
            return []

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
        
    def update(self, mac, updated_device_data):
        if self.collection is None:
            print("Database not connected")
            return False
            
        try:
            if "status" not in updated_device_data:
                existing_device = self.collection.find_one({"mac": mac})
                if existing_device and "status" in existing_device:
                    updated_device_data["status"] = existing_device["status"]
                else:
                    updated_device_data["status"] = "unknown"
            
            updated_device_data["last_updated"] = datetime.now()
                    
            result = self.collection.update_one(
                {"mac": mac},
                {"$set": updated_device_data}
            )
            
            if result.modified_count > 0:
                print(f"Device {mac} updated successfully.")
            else:
                print(f"Device {mac} not updated. No changes made.")
                
            return result.modified_count > 0
        except Exception as e:
            print(f"Failed to update device {mac}: {e}")
            return False
            
    def update_field(self, mac, field, value):
        """Update a single field in a device document"""
        if self.collection is None:
            print("Database not connected")
            return False
            
        try:
            result = self.collection.update_one(
                {"mac": mac},
                {"$set": {field: value, "last_updated": datetime.now()}}
            )
            
            if result.modified_count > 0:
                print(f"Field {field} for device {mac} updated to {value}.")
            else:
                print(f"Field {field} for device {mac} not updated. No changes made.")
                
            return result.modified_count > 0
        except Exception as e:
            print(f"Failed to update field {field} for device {mac}: {e}")
            return False