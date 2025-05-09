from flask import jsonify

class DeviceController:
    def __init__(self, device_service):
        self.device_service = device_service

    def add_new_device(self, scan_data, source):
        try:
            self.device_service.process_scanned_device(scan_data, source)
        except Exception as e:
            print(f"error to add a new device : {e}")

    def list_all_devices(self):
        try:
            devices = self.device_service.list_all_devices()
            for device in devices:
                if '_id' in device:
                    device['_id'] = str(device['_id'])
            return jsonify(devices), 200
        except Exception as e:
            return jsonify({"error": "Error retrieving devices", "details": str(e)}), 500
    
    def get_device_by_mac(self, mac):
        try:
            device = self.device_service.find_device_by_mac(mac)
            
            if device:
                device["_id"] = str(device["_id"])  
                return jsonify(device), 200  
            else:
                return jsonify({"error": "Device not found"}), 404  
        except Exception as e:
            return jsonify({"error": f"Error retrieving device: {str(e)}"}), 500  
 