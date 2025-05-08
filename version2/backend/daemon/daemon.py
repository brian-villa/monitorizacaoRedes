from services.alert_service import AlertService
import threading
import time
from controllers.sniffer_controller import SnifferController
from services.scanner_service import ScannerService

class Daemon:
    def __init__(self, device_service):
        self.device_service = device_service
        self.sniffer_controller = SnifferController(device_service)
        self.scanner_service = ScannerService(device_service)
        self.alert_service = AlertService()  # Inicializando o serviço de alertas

    def run_sniffer(self):
        try:
            self.sniffer_controller.start()
        except Exception as e:
            print(f"[Daemon] Sniffer error: {e}")

    def run_scanner_periodically(self, interval=0.1):
        while True:
            try:
                print("[Daemon] Running scanner...")
                self.scanner_service.scan_network()

                # Simulando uma condição de alerta. Exemplo: novo dispositivo detectado
                # Aqui você pode verificar os dispositivos detectados e gerar alertas
                devices = self.device_service.get_all_devices()  # Obtendo os dispositivos
                for device in devices:
                    if device["mac"] == "00:11:22:33:44:55":  # Exemplo de verificação
                        self.alert_service.generate_alert(
                            mac=device["mac"],
                            title="Suspicious Device Detected",
                            description="The device with MAC 00:11:22:33:44:55 has been detected.",
                            severity="high"
                        )

            except Exception as e:
                print(f"[Daemon] Scanner error: {e}")
            time.sleep(interval)

    def start(self):
        print("[Daemon] Starting background services...")

        # Criação de threads como daemon
        sniffer_thread = threading.Thread(
            target=self.run_sniffer,
            name="SnifferThread"
        )
        scanner_thread = threading.Thread(
            target=self.run_scanner_periodically,
            name="ScannerThread"
        )

        sniffer_thread.daemon = True
        scanner_thread.daemon = True

        sniffer_thread.start()
        scanner_thread.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("[Daemon] Shutting down...")
