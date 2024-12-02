import time
from dbConnect import mongoConnect
from nmap_scan import nmap_scan, save_scan_results
from alert_manager import ensure_alerts_collection, generate_alert


def main():
    db = mongoConnect()

    ensure_alerts_collection(db)
    discovered_devices = set()  # Conjunto para rastrear MACs já encontrados

    while True:
        print("Starting a new network scan...\n")

        # Executa o escaneamento de rede e obtém os resultados
        scan_results = nmap_scan('192.168.1.0/24', "-F")

        # Processa os resultados e verifica se há novos dispositivos
        new_devices = 0
        for device in scan_results:
            mac = device['mac']
            if mac not in discovered_devices:
                discovered_devices.add(mac)
                print(f"New device found: {device}\n")

                # Salva o novo dispositivo no banco
                save_scan_results(db, [device])
                # Gera um alerta para o novo dispositivo
                generate_alert(
                    mac,
                    title="Novo Dispositivo Detectado",
                    description=f"Um novo dispositivo com o MAC {mac} foi encontrado na rede.",
                    severity="medium",
                )

                new_devices += 1

            else:
                print(f"\nDevice already exists: {mac}")

        # Se nenhum novo dispositivo foi encontrado, encerre o loop
        if new_devices == 0:
            print("All devices are already discovered. Stopping scan.")
            break

        # Aguarda 5 minutos antes de uma nova verificação
        time.sleep(300)


if __name__ == "__main__":
    main()
