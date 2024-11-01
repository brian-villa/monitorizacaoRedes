# NÃO ESTOU USANDO ESSE ARQUIVO PQ O SNIFFER FAZ BUSCAR NA REDE EM TEMPO REAL E O NMAP MAPEA TODOS OS DISPOSITIVOS QUE ESTAO CONECTADOS NA REDE E UM SOBREPOE O OUTRO PQ NAO ESTOU CONSEGUINDO CONFIGURAR CORRETAMENTE O SNIFFER E NAO CHAMO ELE NA FUNÇAO MAIN. PORTANTO O NMAP JA CUMPRE O OBJETIVO DE BUSCAR OS DIPOSITIVOS E SALVAR NO DB


from scapy.all import sniff, ARP
from datetime import datetime
from dbConnect import dbCollectionDevice
import socket
import requests

API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImp0aSI6ImVjMDE5YjhiLWM1OTgtNGVjOS1iNzc2LTE0MjFiNTEwYjhmNiJ9.eyJpc3MiOiJtYWN2ZW5kb3JzIiwiYXVkIjoibWFjdmVuZG9ycyIsImp0aSI6ImVjMDE5YjhiLWM1OTgtNGVjOS1iNzc2LTE0MjFiNTEwYjhmNiIsImlhdCI6MTczMDQ5NDMwMSwiZXhwIjoyMDQ0OTkwMzAxLCJzdWIiOiIxNTEzNSIsInR5cCI6ImFjY2VzcyJ9.FvQ_7SJPIcieB-Zc8O2QefFC0qP9-Ls8pIAg7MLSG1M5Ana5r6pkZ9RXqg6UiwxCdCgcVuWmwkRFREn4IS_a4w"

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
            "found_in": datetime.now(),
        }
        print(f"\nDevice found: {device}\n\n")
        print(get_host_name(device_ip))
        # Insert or update device in MongoDB
        dbCollectionDevice(db, device)


def get_manufacturer(mac_address):
    url = f"https://api.macvendors.com/v1/lookup/{mac_address}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json().get("manufacturer", "Unknown Manufacturer")
        else:
            print(f"Failed to get manufacturer. Status Code: {response.status_code}")
            return "Unknown Manufacturer"
    except requests.RequestException as e:
        print(f"Error retrieving manufacturer: {e}")
        return "Unknown Manufacturer"


def get_host_name(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "Unknown"



def start_sniffer(db):
    print("Starting sniffer...")
    sniff(prn=lambda packet: monitorizing_packets(packet, db), filter="arp", store=0)
