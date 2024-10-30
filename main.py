import threading
import time
from dbConnect import mongoConnect
from sniffer import start_sniffer
from nmap_scan import nmap_scan, save_scan_results
from alert_manager import generate_alert

last_scan_devices = set()


def main():
    db = mongoConnect()
    global last_scan_devices

    print("Inicializando monitoramento da rede...")

    sniffer_thread = threading.Thread(target=start_sniffer, args=(db,))
    sniffer_thread.daemon = True
    sniffer_thread.start()

    while True:
        print("Realizando novo escaneamento de rede...")

        scan_results = nmap_scan("192.168.1.0/24")
        current_scan_devices = set(device['mac'] for device in scan_results)

        if not current_scan_devices - last_scan_devices:
            print("Nenhum novo dispositivo detectado. Encerrando escaneamento.")
            break

        last_scan_devices = current_scan_devices
        save_scan_results(db, scan_results)

        for device in scan_results:
            if device.get("status") == "unknown":
                generate_alert(device["mac"], "Dispositivo desconhecido", "Dispositivo não autorizado na rede", "alto",
                               db)

        time.sleep(1000)


if __name__ == "__main__":
    main()
