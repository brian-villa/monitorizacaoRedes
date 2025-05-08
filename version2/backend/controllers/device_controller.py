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
            return self.device_service.list_all_devices()
        except Exception as e:
            return f"Error retrieving devices: {e}"
    
    def get_device_by_mac(self, mac):
        try:
            return self.device_service.find_device_by_mac(mac)
        except Exception as e:
            return f"Error to retrieving a device by mac address: {e}"