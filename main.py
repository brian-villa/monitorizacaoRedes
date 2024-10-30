import threading
import time
from dbConnect import mongoConnect
from sniffer import start_sniffer
from nmap_scan import nmap_scan, save_scan_results
from alert_manager import ensure_alerts_collection

def is_device_new(db, device_mac):
    collection = db['devices']
    return not collection.find_one({"mac": device_mac})

def main():
    db = mongoConnect()
    ensure_alerts_collection(db)

    discovered_devices = set()  # Conjunto para rastrear MACs já encontrados

    print("Starting sniffer...")
    while True:
        print("Starting a new network scan...\n")

        # Executa o escaneamento de rede e obtém os resultados
        scan_results = nmap_scan('192.168.1.0/24')

        # Processa os resultados e verifica se há novos dispositivos
        new_devices = 0
        for device in scan_results:
            mac = device['mac']
            if mac not in discovered_devices:
                discovered_devices.add(mac)
                save_scan_results(db, [device])  # Salva o novo dispositivo no banco
                print(f"New device found: {device}")
                new_devices += 1
            else:
                print(f"Device already exists: {mac}")

        # Se nenhum novo dispositivo foi encontrado, encerre o loop
        if new_devices == 0:
            print("All devices are already discovered. Stopping scan.")
            break

        # Aguarda 5 minutos antes de uma nova verificação
        time.sleep(300)


if __name__ == "__main__":
    main()
