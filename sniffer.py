from scapy.all import sniff, ARP
from datetime import datetime
from dbConnect import mongoConnect, dbCollectionDevice
import socket
import requests


def get_manufacturer(mac_address):
    try:
        response = requests.get(f"https://api.macvendors.com/{mac_address}")
        if response.status_code == 200:
            return response.text.strip()
        return "Unknown Manufacturer"
    except Exception as e:
        print(f"Error retrieving manufacturer: {e}")
        return "Unknown Manufacturer"


def get_host_name(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "Unknown"


def monitorizing_packets(packet, db):
    if packet.haslayer(ARP) and packet[ARP].op == 1:
        device_mac = packet[ARP].hwsrc
        device_ip = packet[ARP].psrc

        # Create device document
        device = {
            "ip": device_ip,
            "mac": device_mac,
            "host": get_host_name(device_ip),
            "manufacturer": get_manufacturer(device_mac),
            "model": "Unknown",
            "found_in": datetime.now(),
            "status": True
        }
        print(f"Device found: {device}")

        # Insert or update device in MongoDB
        dbCollectionDevice(db, device)


def start_sniffer(db):
    print("Starting sniffer...")
    sniff(prn=lambda packet: monitorizing_packets(packet, db), filter="arp", store=0)
