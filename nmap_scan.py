import nmap
from dbConnect import dbCollectionDevice
from datetime import datetime


def nmap_scan(network_range="192.168.1.0/24"):
    print(f"Initializing Nmap scan in {network_range}...")
    scanner = nmap.PortScanner()
    scanner.scan(hosts=network_range, arguments="-sn") #executa o scan

    results = []
    for host in scanner.all_hosts():
        if "mac" in scanner[host]["addresses"]:
            device = {
                "ip": scanner[host]["addresses"].get("ipv4", "Unknown"),
                "mac": scanner[host]["addresses"]["mac"],
                "host": scanner[host].hostname() or "Unknown",
                "status": scanner[host].state(),
                "manufacturer": scanner[host]['vendor'].get(scanner[host]['addresses']['mac'], "Unknown"),
                "found_in": datetime.now()
            }
            results.append(device)
            print(f"Device found: {device}")

    return results


def save_scan_results(db, results):
    for device in results:
        dbCollectionDevice(db, device)
