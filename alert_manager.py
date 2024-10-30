from datetime import datetime

def ensure_alerts_collection(db):
    # Create alerts collection if it doesn't exist
    if "alerts" not in db.list_collection_names():
        db.create_collection("alerts")
        print("Created collection: alerts")

def generate_alert(mac, title, description, severity="medium", db=None):
    alert = {
        "mac": mac,
        "title": title,
        "description": description,
        "severity": severity,
        "timestamp": datetime.now()
    }
    print(f"Alert generated: {alert}")

    if db:
        db["alerts"].insert_one(alert)
        print(f"Alert inserted successfully: {alert}") ##Ver pq nao cria a tabela no data base
