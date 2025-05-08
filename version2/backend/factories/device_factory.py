from models.device_model import DeviceModel
from datetime import datetime

class DeviceFactory:
    @staticmethod
    def from_scanner(scan_data: dict, source: str) -> DeviceModel:
        return DeviceModel(
            ip=scan_data.get("ip", "0.0.0.0"),
            mac=scan_data.get("mac", "00:00:00:00:00:00").upper(),
            host=scan_data.get("host", None),
            status=scan_data.get("status", "unknown"),
            manufacturer=scan_data.get("manufacturer", "unknown"),
            found_in=source,
            created_at=datetime.now()
        )
