from factories.device_factory import DeviceFactory


class DeviceService:
    def __init__(self, repository): 
        self.repository = repository

    def process_scanned_device(self, scan_data, source):
        try:
            device = DeviceFactory.from_scanner(scan_data, source)
            device_dict = device.device_schema()
            return self.repository.insert(device_dict)
        except Exception as e:
            print(f"Error processing device: {e}")
            return False

    def list_all_devices(self):
        try:
            return self.repository.get_all()
        except Exception as e:
            print(f"Error listing devices: {e}")
            return []

    def find_device_by_mac(self, mac):
        try:
            return self.repository.find_by_mac(mac)
        except Exception as e:
            print(f"Error finding device by MAC: {e}")
            return None