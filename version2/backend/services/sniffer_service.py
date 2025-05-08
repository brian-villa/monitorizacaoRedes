from scapy.all import sniff, ARP
from datetime import datetime
from db.db_connection import MongoDBConnection
from repositories.device_repository import DeviceRepository
import socket
import requests


class SnifferService:
    def __init__(self, device_service, api_key):
        self.device_service = device_service
        self.api_key = api_key

    def start_sniffer(self):
        print("Starting sniffer...")
        sniff(prn=self.process_packet, filter="arp", store=0)

    def process_packet(self, packet):
        if packet.haslayer(ARP) and packet[ARP].op == 1:
            mac = packet[ARP].hwsrc
            ip = packet[ARP].psrc

            device_data = {
                "ip": ip,
                "mac": mac.upper(),
                "host": self.resolve_host(ip),
                "manufacturer": self.get_manufacturer(mac),
                "found_in": "sniffer"
            }
            
            self.device_service.process_scanned_device(device_data, "sniffer")

    def get_manufacturer(self, mac_address):
        try:
            url = f"https://api.macvendors.com/v1/lookup/{mac_address}"
            headers = {"Authorization": f"Bearer {self.api_key}"}
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response.json().get("manufacturer", "Unknown")
            return "Unknown"
        except Exception as e:
            print(f"[Sniffer] Error getting manufacturer: {e}")
            return "Unknown"

    def resolve_host(self, ip):
        try:
            return socket.gethostbyaddr(ip)[0]
        except socket.herror:
            return "Unknown"
