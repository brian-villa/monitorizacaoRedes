from flask import Flask, jsonify
from flask_cors import CORS
from dbConnect import mongoConnect
import traceback  # Para logs detalhados de erro

app = Flask(__name__)
# Configuração mais robusta do CORS
CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)

# Conexão com o MongoDB
db = mongoConnect()

# Endpoint para obter dispositivos com tratamento de erro
@app.route("/api/devices", methods=["GET"])
def get_devices():
    try:
        devices_collection = db["devices"]
        devices = list(devices_collection.find({}, {"_id": 0}))
        return jsonify(devices)
    except Exception as e:
        print(f"Erro ao acessar MongoDB: {e}")
        print(traceback.format_exc())  # Imprime o stack trace completo
        return jsonify({"error": str(e)}), 500

# Manipulador de erro para garantir CORS em respostas de erro
@app.errorhandler(500)
def handle_500(e):
    response = jsonify({"error": "Internal Server Error", "details": str(e)})
    response.status_code = 500
    return response

# Inicia o servidor
if __name__ == "__main__":
    app.run(debug=True)