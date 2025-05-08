from pymongo import MongoClient
import os
from dotenv import load_dotenv

from pathlib import Path

dotenv_path = Path(__file__).resolve().parents[3] / ".env.local"
print(dotenv_path)

loaded = load_dotenv(dotenv_path)
print(f".env carregado? {loaded}")




mongo_uri = os.getenv('mongodb')
print(f"URI do MongoDB: {mongo_uri}")

try:
  
    client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
   
    
    # Verificar conexão
    client.server_info()
    
    print("Conexão bem-sucedida!")
    
    # Listar bancos de dados disponíveis
    print("Bancos de dados disponíveis:")
    for db_name in client.list_database_names():
        print(f" - {db_name}")
    
    client.close()
    
except Exception as e:
    print(f"Erro ao conectar: {e}")