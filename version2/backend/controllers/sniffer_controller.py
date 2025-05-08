from services.sniffer_service import SnifferService

from dotenv import load_dotenv

from pathlib import Path
dotenv_path = Path(__file__).resolve().parents[3] / ".env.local"
load_dotenv(dotenv_path)

class SnifferController:
    def __init__(self, device_service):
        self.device_service = device_service
        self.service = SnifferService(device_service, api_key="MAC_VENDORS")

    def start(self):
        try:
            self.service.start_sniffer()
        except KeyboardInterrupt:
            print("\n[SnifferController] Sniffer stopped by user.")
        except Exception as e:
            print(f"[SnifferController] Error running sniffer: {e}")
