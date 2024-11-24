import nmap
from dbConnect import dbCollectionDevice
from datetime import datetime



def nmap_scan(network_range, port):
    network_range = "172.31.0.0/24"
    port = "-F"  # -F para portas comuns ou "-p-" para todas as portas

    print(f"Initializing Nmap scan in {network_range}...")
    scanner = nmap.PortScanner()
    scanner.scan(hosts=network_range, arguments=port) #executa o scan

    #print(dir(scanner)) #utilizar o all_hosts retornado

    results = []
    for host in scanner.all_hosts():
        #print(scanner.all_hosts()) #Ver portas comuns e buscar dispositivos conectados
        #print(scanner[host]["addresses"]) #infos dos devices em rede
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
            #print(f"Devices found: {device}")

    return results


def save_scan_results(db, results):
    for device in results:
        dbCollectionDevice(db, device)
