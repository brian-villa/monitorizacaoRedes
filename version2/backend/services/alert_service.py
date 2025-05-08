from db.db_connection import MongoDBConnection
from repositories.alert_repository import AlertRepository
from factories.alert_factory import AlertFactory
from datetime import datetime

class AlertService:
    def __init__(self):
        db = MongoDBConnection().get_db()
        self.repository = AlertRepository(db)

    def generate_alert(self, mac, title, description, severity="medium"):
        try:
            alert = AlertFactory.create(mac, title, description, severity)
            alert_data = alert.alert_schema()
            self.repository.insert_one(alert_data)
            print(f"\nAlert inserted successfully: {alert}\n")
        except Exception as e:
            print(f"\nError inserting alert: {e}\n")

    def get_alerts_by_mac(self, mac):
        return self.repository.find_by_mac(mac)

    def get_all_alerts(self):
        return self.repository.find_all()
