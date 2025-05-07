import nmap
from app.factories.device_factory import DeviceFactory
from app.services.device_service import DeviceService

class ScannerService:
    def __init__(self):
        self.scanner = nmap.PortScanner()
        self.device_service = DeviceService()

    def scan_network(self, network_range="192.168.0.0/24", ports="-F"):
        print(f"Running Nmap scan on {network_range}")
        self.scanner.scan(hosts=network_range, arguments=ports)

        devices = []
        for host in self.scanner.all_hosts():
            addresses = self.scanner[host].get("addresses", {})
            mac = addresses.get("mac")
            if mac:
                device_data = {
                    "ip": addresses.get("ipv4", "Unknown"),
                    "mac": mac,
                    "host": self.scanner[host].hostname(),
                    "status": self.scanner[host].state(),
                    "manufacturer": self.scanner[host]["vendor"].get(mac, "Unknown")
                }
                device = DeviceFactory.from_scanner(device_data, source="nmap")
                self.device_service.save_device(device)
                devices.append(device)

        return devices