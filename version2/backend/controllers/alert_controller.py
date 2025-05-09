from services.alert_service import AlertService
from flask import jsonify

class AlertController:
    def __init__(self):
        self.alert_service = AlertService()

    def create_alert(self, mac, title, description, severity="medium"):
        return self.alert_service.generate_alert(mac, title, description, severity)

    def list_alerts_by_mac(self, mac):
        try:
            alerts = self.alert_service.get_alerts_by_mac(mac)
            for alert in alerts:
                if '_id' in alert:
                    alert['_id'] = str(alert['_id'])
            return jsonify(alerts), 200
        except Exception as e:
            return jsonify({"error": "Error retrieving alerts", "details": str(e)}), 500

    def list_all_alerts(self):
        try:
            alerts = self.alert_service.get_all_alerts()
            for alert in alerts:
                if '_id' in alert:
                    alert['_id'] = str(alert['_id'])
            return jsonify(alerts), 200
        except Exception as e:
            return jsonify({"error": "Error retrieving alerts", "details": str(e)}), 500
