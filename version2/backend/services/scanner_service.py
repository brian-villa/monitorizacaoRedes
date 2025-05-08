import nmap
from factories.device_factory import DeviceFactory
from services.device_service import DeviceService

class ScannerService:
    def __init__(self, device_service):  # Recebe o service por injeção
        self.scanner = nmap.PortScanner()
        self.device_service = device_service

    def scan_network(self, network_range="192.168.0.0/24", ports="-F"):
        print(f"Running Nmap scan on {network_range}")
        self.scanner.scan(hosts=network_range, arguments=ports)

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
                self.device_service.process_scanned_device(device_data, "nmap")