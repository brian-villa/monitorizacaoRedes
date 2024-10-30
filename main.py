import threading
import time
from dbConnect import mongoConnect
from sniffer import start_sniffer
from nmap_scan import nmap_scan, save_scan_results

def is_device_new(db, device_mac):
    collection = db['devices']
    return not collection.find_one({"mac": device_mac})

def main():
    db = mongoConnect()

    sniffer_thread = threading.Thread(target=start_sniffer, args=(db,))
    sniffer_thread.daemon = True
    sniffer_thread.start()

    while True:
        print("Starting a new network scan...\n")
        scan_results = nmap_scan("192.168.1.0/24")
        new_device_found = False

        for device in scan_results:
            device_mac = device.get("mac")
            if is_device_new(db, device_mac):
                new_device_found = True
                save_scan_results(db, [device])

        if not new_device_found:
            print("No new devices found.\n")
            break

        time.sleep(300)

if __name__ == "__main__":
    main()
