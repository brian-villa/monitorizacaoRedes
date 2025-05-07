import sys
import os
import threading
import time

# Obtenha o caminho absoluto para o diretório raiz do projeto (backend)
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(BASE_DIR)

from app.daemon.daemon import Daemon
from app.api.api import FlaskAPI

class Application:
    def __init__(self):
        self.flask_api = FlaskAPI()

    def start(self):
        api_thread = threading.Thread(target=self.flask_api.run, kwargs={'debug': True, 'host': '0.0.0.0', 'port': 5000})
        api_thread.daemon = True
        api_thread.start()

        daemon = Daemon()
        daemon.start()

        
        while True:
            time.sleep(1)

if __name__ == "__main__":
    application = Application()
    application.start()
