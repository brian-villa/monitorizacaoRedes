from model.deviceModel import DeviceModel

class DeviceController:
    def __init__(self):
        self.device_model = DeviceModel()

    def add_device(self, device):
        try:
            if not device["mac"]:
                return "Error: Device MAC address is required."
            
            self.device_model.save_device(device)
            return f"Device with MAC {device["mac"]} processed."
        except Exception as e:
            return f"Error processing device: {e}"

    def list_device(self):
        try:
            devices = self.device_model.get_all_devices()
            return devices if devices else "No devices found"
        except Exception as e:
            return f"Error retrieving devices: {e}"