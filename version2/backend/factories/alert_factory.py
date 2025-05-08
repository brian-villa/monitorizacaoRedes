from models.alert_model import AlertModel
from datetime import datetime

class AlertFactory:
    @staticmethod
    def create(mac, title, description, severity="medium") -> AlertModel:
        return AlertModel(
            mac=mac,
            title=title,
            description=description,
            severity=severity,
            alert_generated_at=datetime.now()
        )
