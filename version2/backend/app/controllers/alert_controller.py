from app.services.alert_service import AlertService

class AlertController:
    def __init__(self):
        self.alert_service = AlertService()

    def create_alert(self, mac, title, description, severity="medium"):
        return self.alert_service.generate_alert(mac, title, description, severity)

    def list_alerts_by_mac(self, mac):
        return self.alert_service.get_alerts_by_mac(mac)

    def list_all_alerts(self):
        return self.alert_service.get_all_alerts()
