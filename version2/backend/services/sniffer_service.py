from services.alert_service import AlertService
from scapy.all import sniff, ARP
import socket
import requests
from datetime import datetime

class SnifferService:
    def __init__(self, device_service, api_key):
        self.device_service = device_service
        self.api_key = api_key
        self.alert_service = AlertService()
        self.manufacturer_cache = {}

    def start_sniffer(self):
        print("Starting sniffer...")
        sniff(prn=self.process_packet, filter="arp", store=0)

    def process_packet(self, packet):
        if packet.haslayer(ARP) and packet[ARP].op == 1:
            mac = packet[ARP].hwsrc.upper()
            ip = packet[ARP].psrc

            is_new_device = self.device_service.is_device_new(mac)

            manufacturer = self.get_or_cache_manufacturer(mac, is_new_device)

            device_data = {
                "ip": ip,
                "mac": mac,
                "host": self.resolve_host(ip),
                "manufacturer": manufacturer,
                "found_in": "sniffer",
                "status": "active",
                "last_seen": datetime.now()
            }

            status_changed = self.device_service.update_device_status(mac, "active")
            self.device_service.process_scanned_device(device_data, "sniffer")

            self.create_alerts_for_device(mac, ip, device_data, is_new_device, status_changed)

    def get_or_cache_manufacturer(self, mac, is_new):
        if not is_new:
            existing_device = self.device_service.find_device_by_mac(mac)
            if existing_device and existing_device.get("manufacturer") != "Unknown":
                return existing_device["manufacturer"]
            if mac in self.manufacturer_cache:
                return self.manufacturer_cache[mac]

        manufacturer = self.get_manufacturer(mac)
        self.manufacturer_cache[mac] = manufacturer
        return manufacturer

    def create_alerts_for_device(self, mac, ip, device_data, is_new_device, status_changed):
        suspicious_macs = ["00:11:22:33:44:55", "AA:BB:CC:DD:EE:FF"]

        if is_new_device:
            self.alert_service.generate_alert(
                mac=mac,
                title="New Device Detected",
                description=f"New device with IP {ip} and MAC {mac} detected.",
                severity="medium"
            )

        if mac in suspicious_macs:
            self.alert_service.generate_alert(
                mac=mac,
                title="Suspicious Device Detected",
                description=f"Suspicious MAC {mac} detected.",
                severity="high"
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

    def get_manufacturer(self, mac):
        try:
            url = f"https://api.macvendors.com/{mac}"
            headers = {"Authorization": f"Bearer {self.api_key}"}
            response = requests.get(url, headers=headers)
            return response.text if response.status_code == 200 else "Unknown"
        except Exception as e:
            print(f"Error fetching manufacturer: {e}")
            return "Unknown"

    def resolve_host(self, ip):
        try:
            return socket.gethostbyaddr(ip)[0]
        except socket.herror:
            return "Unknown"
