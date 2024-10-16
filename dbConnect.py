from pymongo import MongoClient
from datetime import datetime

#Connect to database (localhost ou instância remota)
client = MongoClient("localhost", 27017)
db = client["ProjetoADMRedesBD"] #db name
collection = db["trafego_rede"]

#function to save mongodb packages

def save_package_mongo(ip_origem, ip_destino, protocolo, tamanho_pacote) : pacote {
    'ip_origem': ip_origem,
    'ip_destino': ip_destino,
    'protocolo': protocolo,
    'tamanho_pacote': tamanho_pacote,
    'timestamp': datetime.now()
}
try:
    collection.insert_one(pacote)
    print("Pacote salvo no Mongodb")
except Exception as e:
    print(f"Erro ao salvar no MongoDB: {e}")
