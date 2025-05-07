
from app.services.sniffer_service import SnifferService

class SnifferController:
    def __init__(self):
        self.service = SnifferService()

    def start(self):
        try:
            self.service.start_sniffer()
        except KeyboardInterrupt:
            print("\n[SnifferController] Sniffer stopped by user.")
        except Exception as e:
            print(f"[SnifferController] Error running sniffer: {e}")
