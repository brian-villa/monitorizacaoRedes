import sys
import os
import threading
import time

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(BASE_DIR)

from db.db_connection import MongoDBConnection
from repositories.device_repository import DeviceRepository
from services.device_service import DeviceService
from api.api import FlaskAPI
from daemon.daemon import Daemon

class Application:
    def __init__(self):
        self.db_connection = MongoDBConnection()
        
        self.device_repository = DeviceRepository(self.db_connection)
        self.device_service = DeviceService(self.device_repository)
        
        self.flask_api = FlaskAPI(self.device_service)
        self.daemon = Daemon(self.device_service)

    def start(self):
        try:
            print("Starting Flask API...")
            api_thread = threading.Thread(
                target=self.flask_api.run,
                kwargs={'debug': False, 'use_reloader': False},
                name="FlaskThread"
            )
            api_thread.daemon = True
            api_thread.start()

            print("Starting Daemon...")
            self.daemon.start()

            while True:
                time.sleep(1)
                
        except KeyboardInterrupt:
            print("\nShutting down application...")
            self.db_connection.close_connection()
        except Exception as e:
            print(f"Application error: {e}")
            self.db_connection.close_connection()

if __name__ == "__main__":
    application = Application()
    application.start()
