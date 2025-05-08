from flask import Flask, jsonify
from flask_cors import CORS
from db.db_connection import MongoDBConnection
from repositories.device_repository import DeviceRepository
from services.device_service import DeviceService
from controllers.device_controller import DeviceController

class FlaskAPI:
    def __init__(self, device_service):
        self.app = Flask(__name__)
        self.device_service = device_service
        self.configure_app()
        self.setup_database()
        #self.setup_services()
        self.setup_controllers()
        self.register_routes()
        self.register_error_handlers()

    def configure_app(self):
        #CORS
        CORS(self.app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)

    def setup_database(self):
        try:
            self.db_connection = MongoDBConnection()
            if self.db_connection.get_db() is None:
                print("WARNING: API initialized without database connection.")
        except Exception as e:
            print(f"Error configuring database connection: {e}")
            self.db_connection = None

    def setup_services(self):
        try:
            device_repo = DeviceRepository(self.db_connection)
            self.device_service = DeviceService(device_repo)
        except Exception as e:
            print(f"Error configuring services: {e}")
            self.device_service = None

    def setup_controllers(self):
        try:
            self.device_controller = DeviceController(self.device_service)  # Inject the service
        except Exception as e:
            print(f"Error configuring controllers: {e}")
            self.device_controller = None

    def register_routes(self):
        #check API status
        @self.app.route("/api/status", methods=["GET"])
        def get_status():
            db_status = "connected" if self.db_connection and self.db_connection.get_db() else "disconnected"
            return jsonify({
                "status": "online",
                "database": db_status
            })

        #get devices
        @self.app.route("/api/devices", methods=["GET"])
        def get_devices():
            if not self.device_controller:
                return jsonify({"error": "Device controller not available"}), 503
            return self.device_controller.list_all_devices()

    def register_error_handlers(self):
        @self.app.errorhandler(500)
        def handle_500(e):
            response = jsonify({"error": "Internal Server Error", "details": str(e)})
            response.status_code = 500
            return response

        @self.app.errorhandler(404)
        def handle_404(e):
            response = jsonify({"error": "Not Found", "details": str(e)})
            response.status_code = 404
            return response

    def run(self, debug=True, host='0.0.0.0', port=5000, use_reloader=False):
        try:
            print(f"Starting Flask API at http://{host}:{port}")
            self.app.run(debug=debug, host=host, port=port, use_reloader=use_reloader)
        except Exception as e:
            print(f"Error starting the API: {e}")
        finally:
            if hasattr(self, 'db_connection') and self.db_connection:
                self.db_connection.close_connection()