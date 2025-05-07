import threading
import time
from controllers.sniffer_controller import SnifferController
from services.scanner_service import ScannerService

class Daemon:
    def __init__(self):
        self.sniffer_controller = SnifferController()
        self.scanner_service = ScannerService()

    def run_sniffer(self):
        self.sniffer_controller.start()

    def run_scanner_periodically(self, interval=30):  # 5 minutos
        while True:
            print("[Daemon] Running scanner...")
            self.scanner_controller.scan()
            time.sleep(interval)

    def start(self):
        print("[Daemon] Starting background services...")

        sniffer_thread = threading.Thread(target=self.run_sniffer)
        scanner_thread = threading.Thread(target=self.run_scanner_periodically)

        sniffer_thread.daemon = True
        scanner_thread.daemon = True

        sniffer_thread.start()
        scanner_thread.start()

        while True:
            time.sleep(1)  # mantém o processo vivo