
class AlertRepository:
    def __init__(self, db):
        self.collection = db["alerts"]
    
    def insert(self, alert:dict):
        try:
            self.collection.insert_one(alert)
            print(f"Alert inserted: {alert.get("title")}")
        except Exception as e:
            print(f"failed to insert a Alert {e}")

    def find_by_mac(self, mac):
        return list(self.collection.find({"mac": mac}))
    
    def find_all(self):
        return list(self.collection.find())
    
    