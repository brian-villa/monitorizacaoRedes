from datetime import datetime

def ensure_alerts_collection(db):
    try:
        # Create alerts collection if it doesn't exist
        if "alerts" not in db.list_collection_names():
            db.create_collection("alerts")
            print("Created collection: alerts")
    except Exception as e:
        print(f"Error creating 'alerts' collection: {e}")

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
        print(f"Alert inserted successfully: {alert}")
