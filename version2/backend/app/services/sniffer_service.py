from scapy.all import sniff, ARP
from datetime import datetime
from app.db.db_connection import MongoDBConnection
from app.repositories.device_repository import DeviceRepository
import socket
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class SnifferService:
    def __init__(self):
        db = MongoDBConnection().get_db()
        self.repository = DeviceRepository(db)
        self.api_key = os.getenv("api_key_mac_vendors")

    def start_sniffer(self):
        print("Starting sniffer...")
        sniff(prn=self.process_packet, filter="arp", store=0)

    def process_packet(self, packet):
        if packet.haslayer(ARP) and packet[ARP].op == 1:
            mac = packet[ARP].hwsrc
            ip = packet[ARP].psrc

            device = {
                "ip": ip,
                "mac": mac.upper(),
                "host": self.resolve_host(ip),
                "manufacturer": self.get_manufacturer(mac),
                "found_in": "sniffer",
                "created_at": datetime.now()
            }

            print(f"[Sniffer] Device found: {device}")
            self.repository.insert_if_not_exists(device)

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
