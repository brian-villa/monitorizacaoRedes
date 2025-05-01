from app.db.db_connection import MongoDBConnection
from app.repositories.device_repository import DeviceRepository
from app.factories.device_factory import DeviceFactory

class DeviceService:
    def __init__(self):
        db = MongoDBConnection().get_db()
        self.repository = DeviceRepository(db)

    def process_scanned_device(self, scan_data, source):
        device = DeviceFactory.from_scanner(scan_data, source)
        device_dict = device.device_schema()
        self.repository.insert(device_dict)

    def list_all_devices(self):
        return self.repository.get_all()
    
    def find_device_by_mac(self,mac):
        return self.repository.find_by_mac(mac)
    