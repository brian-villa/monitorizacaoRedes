from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# Conexão com o MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["monitorizing_network"]

# Endpoint para obter dispositivos
@app.route("/api/devices", methods=["GET"])
def get_devices():
    devices_collection = db["devices"]
    devices = list(devices_collection.find({}, {"_id": 0})) # vai excluir o id dos campos enviados
    return jsonify(devices)

# Inicia o servidor
if __name__ == "__main__":
    app.run(debug=True)
