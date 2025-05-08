from datetime import datetime

class DeviceModel:
    def __init__(self, ip, mac, host, status, manufacturer, found_in=None, created_at=None):
        self.ip = ip
        self.mac = mac
        self.host = host
        self.status = status
        self.manufacturer = manufacturer
        self.found_in = found_in
        self.created_at = created_at or datetime.now()
    
    def device_schema(self):
        return {
            "ip": self.ip,
            "mac": self.mac,
            "host": self.host,
            "status": self.status,
            "manufacturer": self.manufacturer,
            "found_in": self.found_in,
            "crated_at": self.created_at
        }
    
    def __str__(self):
        return f"Device: ip: {self.ip}, mac:{self.mac}, host: {self.host}, status: {self.status}, manufacturer: {self.manufacturer}, found_in: {self.found_in}, created_at: {self.created_at}"