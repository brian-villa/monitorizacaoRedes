import threading
import time
from controllers.sniffer_controller import SnifferController
from services.scanner_service import ScannerService

class Daemon:
    def __init__(self, device_service):
        self.device_service = device_service
        self.sniffer_controller = SnifferController(device_service)
        self.scanner_service = ScannerService(device_service)

    def run_sniffer(self):
        try:
            self.sniffer_controller.start()
        except Exception as e:
            print(f"[Daemon] Sniffer error: {e}")

    def run_scanner_periodically(self, interval=30):
        while True:
            try:
                print("[Daemon] Running scanner...")
                self.scanner_service.scan_network()
            except Exception as e:
                print(f"[Daemon] Scanner error: {e}")
            time.sleep(interval)

    def start(self):
        print("[Daemon] Starting background services...")

        #threads como daemon
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