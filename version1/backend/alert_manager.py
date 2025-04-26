from datetime import datetime
from dbConnect import mongoConnect

db = mongoConnect()

def ensure_alerts_collection(db):

    try:
        # Create alerts collection if it doesn't exist
        if "alerts" not in db.list_collection_names():
            db.create_collection("alerts")
            print("Created collection: alerts")
    except Exception as e:
        print(f"\nError creating 'alerts' collection: {e}")

def generate_alert(mac, title, description, severity="medium"):
    alert = {
        "mac": mac,
        "title": title,
        "description": description,
        "severity": severity,
        "timestamp": datetime.now()
    }
    print(f"Alert generated: {alert}")

    try:
        db["alerts"].insert_one(alert)
        print(f"\nAlert inserted successfully: {alert}\n")
    except Exception as e:
        print(f"\nError inserting alert: {e}\n")