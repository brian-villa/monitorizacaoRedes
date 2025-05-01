from datetime import datetime

class AlertModel:
    def __init__(self, mac, title, description, severity=None, alert_generated_at=None):
        self.mac = mac,
        self.title = title,
        self.description = description,
        self.severity = severity,
        self.alert_generated_at = alert_generated_at or datetime.now()
    def alert_schema(self):
        return {
            "mac": self.mac,
            "title": self.title,
            "description": self.description,
            "severity": self.severity,
            "alert_generated_at": self.alert_generated_at
        }
    def __str__(self):
        return f"Alert: mac: {self.mac}, title: {self.title}, description: {self.description}, severity: {self.severity}, alert_generated_at: {self.alert_generated_at}"
    
        