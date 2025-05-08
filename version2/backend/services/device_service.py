from factories.device_factory import DeviceFactory
from datetime import datetime

class DeviceService:
    def __init__(self, device_repository):
        self.device_repository = device_repository
    
    def process_scanned_device(self, device_data, source):
        if "status" not in device_data:
            device_data["status"] = "unknown"

        if "last_updated" not in device_data:
            device_data["last_updated"] = datetime.now()
            
        existing_device = self.device_repository.find_by_mac(device_data["mac"])
        if existing_device:

            for field in ["first_seen", "alerts_count"]:
                if field in existing_device and field not in device_data:
                    device_data[field] = existing_device[field]
                    
            self.device_repository.update(device_data["mac"], device_data)
        else:
            device_data["first_seen"] = datetime.now()
            device_data["alerts_count"] = 0
            self.device_repository.insert(device_data)
    
    def update_device_status(self, mac, new_status):
        if new_status in ["up", "active"]:
            standardized_status = "active"
        elif new_status in ["down", "inactive"]:
            standardized_status = "inactive"
        else:
            standardized_status = new_status
            
        existing_device = self.device_repository.find_by_mac(mac)
        if existing_device:
            old_status = existing_device.get("status", "unknown")
            print(f"Existing status: {old_status}, New status: {standardized_status}")

            if old_status != standardized_status:
                existing_device["status"] = standardized_status
                existing_device["last_status_change"] = datetime.now()
                self.device_repository.update(mac, existing_device)
                print(f"Updated device {mac} status from {old_status} to {standardized_status}")
                return True 
            else:
                print(f"Status is already {standardized_status}, no update needed.")
                return False  
        else:
            print(f"Device with MAC {mac} not found in the database.")
            minimal_device = {
                "mac": mac,
                "status": standardized_status,
                "found_in": "status_update",
                "first_seen": datetime.now(),
                "last_seen": datetime.now(),
                "last_status_change": datetime.now(),
                "alerts_count": 0
            }
            print(f"Creating new device with MAC {mac} and status {standardized_status}")
            self.device_repository.insert(minimal_device)
            return True 
    
    def is_device_new(self, mac):
        existing_device = self.device_repository.find_by_mac(mac)
        return existing_device is None
    
    def get_all_devices(self):
        try:
            return self.device_repository.get_all()
        except Exception as e:
            print(f"Error listing devices: {e}")
            return []
    
    def list_all_devices(self):
        return self.get_all_devices()
    
    def find_device_by_mac(self, mac):
        try:
            return self.device_repository.find_by_mac(mac)
        except Exception as e:
            print(f"Error finding device by MAC: {e}")
            return None
        
    def get_active_devices(self):
        """Get all devices with status 'active'"""
        try:
            return self.device_repository.find_by_status("active")
        except Exception as e:
            print(f"Error finding active devices: {e}")
            return []
            
    def get_inactive_devices(self):
        """Get all devices with status 'inactive'"""
        try:
            return self.device_repository.find_by_status("inactive")
        except Exception as e:
            print(f"Error finding inactive devices: {e}")
            return []
    
    def increment_alert_count(self, mac):
        """Increment the alert count for a device"""
        device = self.device_repository.find_by_mac(mac)
        if device:
            alerts_count = device.get("alerts_count", 0) + 1
            self.device_repository.update_field(mac, "alerts_count", alerts_count)
            return alerts_count
        return 0