from flask import Flask, jsonify
from flask_cors import CORS
from app.db.db_connection import MongoDBConnection
from app.repositories.device_repository import DeviceRepository
from app.controllers.device_controller import DeviceController

class FlaskAPI:
    def __init__(self):
        self.app = Flask(__name__)
        self.configure_app()
        self.setup_database()
        self.setup_repositories()
        self.setup_controllers()
        self.register_routes()
        self.register_error_handlers()
        
    def configure_app(self):
        # Configuração do CORS
        CORS(self.app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)
        
    def setup_database(self):
        self.db_connection = MongoDBConnection()
        
    def setup_repositories(self):
        self.device_repository = DeviceRepository(self.db_connection)
        
    def setup_controllers(self):
        self.device_controller = DeviceController(self.device_repository)
        
    def register_routes(self):
        # Endpoint para obter dispositivos
        @self.app.route("/api/devices", methods=["GET"])
        def get_devices():
            return self.device_controller.get_all_devices()
            
    def register_error_handlers(self):
        @self.app.errorhandler(500)
        def handle_500(e):
            response = jsonify({"error": "Internal Server Error", "details": str(e)})
            response.status_code = 500
            return response
            
    def run(self, debug=True, host='0.0.0.0', port=5000):
        try:
            self.app.run(debug=debug, host=host, port=port)
        finally:
            # Garante que a conexão com o MongoDB seja fechada ao encerrar
            self.db_connection.close_connection()