from scapy.all import sniff, ARP
from datetime import datetime
from dbConnect import mongoConnect, dbCollectionDevice
from getmac import get_mac_address
import socket
import nmap


def get_device_info(mac):
    #get the manufact by mac andress
    manufacturer = get_mac_address(mac)
    return manufacturer

def get_host_name(ip):
    try:
        host = socket.gethostbyaddr(ip)[0]
    except socket.herror:
        host = "Unknown"
    return host

def monitorizing_packets(packet):
    device_mac = packet[ARP].hwsrc
    device_ip = packet[ARP].psrc

    if packet.haslayer(ARP) and packet[ARP].op == 1:
        device = {
            "ip": packet[ARP].psrc,
            "mac": packet[ARP].hwsrc,
            "host": get_host_name(device_ip),
            "manufacturer": get_device_info(device_mac),
            "model": "Unknown",
            "found_in": datetime.now()
        }
    print(f"Device found: {device}")

    db=mongoConnect() #conecta ao mongodb
    dbCollectionDevice(db, device)


def start_sniffer():
    print("Starting sniffer...")
    sniff(prn=monitorizing_packets, filter="arp", store=0)

if __name__ == "__main__":
    start_sniffer()
