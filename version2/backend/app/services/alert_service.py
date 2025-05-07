from app.db.db_connection import MongoDBConnection
from app.repositories.alert_repository import AlertRepository
from app.factories.alert_factory import AlertFactory
from datetime import datetime
class AlertService:
    def __init__(self):
        db = MongoDBConnection().get_db()
        self.repository = AlertRepository(db)

    def generate_alert(self, mac, title, description, severity="medium"):
        alert = {
            "mac": mac,
            "title": title,
            "description": description,
            "severity": severity,
            "alert_generated_at": datetime.now()
        }
        print(f"Alert generated: {alert}")

        try:
            self.collection.insert_one(alert)
            print(f"\nAlert inserted successfully: {alert}\n")
        except Exception as e:
            print(f"\nError inserting alert: {e}\n")

    def get_alerts_by_mac(self, mac):
        return self.repository.find_by_mac(mac)

    def get_all_alerts(self):
        return self.repository.find_all()
