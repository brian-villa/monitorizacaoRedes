import nmap
from datetime import datetime
from services.alert_service import AlertService

class ScannerService:
    def __init__(self, device_service):
        self.scanner = nmap.PortScanner()
        self.device_service = device_service
        self.alert_service = AlertService()
        self.previously_seen_devices = set()

    def scan_network(self, network_range="172.31.0.0/24", ports="-PR"):
        print(f"Running Nmap scan on {network_range}")
        self.scanner.scan(hosts=network_range, arguments=ports)

        current_scan_devices = set()

        for host in self.scanner.all_hosts():
            addresses = self.scanner[host].get("addresses", {})
            mac = addresses.get("mac")
            ip = addresses.get("ipv4", "Unknown")

            if mac:
                mac = mac.upper()
                current_scan_devices.add(mac)

                is_new_device = self.device_service.is_device_new(mac)
                nmap_state = self.scanner[host].state()
                status = "active" if nmap_state == "up" else "inactive"

                device_data = {
                    "ip": ip,
                    "mac": mac,
                    "host": self.scanner[host].hostname(),
                    "status": status,
                    "manufacturer": self.scanner[host]["vendor"].get(mac, "Unknown"),
                    "found_in": "nmap",
                    "last_seen": datetime.now()
                }

                status_changed = self.device_service.update_device_status(mac, status)
                self.device_service.process_scanned_device(device_data, "nmap")
                self.create_alerts_if_needed(mac, ip, device_data, is_new_device, status_changed)

                self.previously_seen_devices.add(mac)

        missing_devices = self.previously_seen_devices - current_scan_devices
        for mac in missing_devices:
            device = self.device_service.find_device_by_mac(mac)
            if device:
                ip = device.get("ip", "Unknown")
                was_updated = self.device_service.update_device_status(mac, "inactive")
                if was_updated:
                    self.alert_service.generate_alert(
                        mac=mac,
                        title="Device Missing",
                        description=f"Device with MAC {mac} and IP {ip} is no longer visible.",
                        severity="medium"
                    )

    def create_alerts_if_needed(self, mac, ip, device_data, is_new_device, status_changed):
        if is_new_device:
            self.alert_service.generate_alert(
                mac=mac,
                title="New Device Detected",
                description=f"New device with IP {ip} and MAC {mac} detected via Nmap.",
                severity="medium"
            )

        if device_data["manufacturer"] == "Unknown":
            existing_device = self.device_service.find_device_by_mac(mac)
            if not existing_device.get("unknown_manufacturer_alerted", False):
                self.alert_service.generate_alert(
                    mac=mac,
                    title="Unknown Manufacturer",
                    description=f"Device with MAC {mac} has an unknown manufacturer.",
                    severity="low"
                )
                self.device_service.device_repository.update_field(mac, "unknown_manufacturer_alerted", True)

        if status_changed and device_data["status"] == "inactive":
            self.alert_service.generate_alert(
                mac=mac,
                title="Device Inactive",
                description=f"Device with MAC {mac} is inactive.",
                severity="low"
            )
