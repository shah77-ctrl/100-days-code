import datetime
import socket

target = input("Target IP: ")
ports_input = input("Port nak scan (contoh: 22,80,443): ")
ports_list = ports_input.split(",")

with open("scan.log", "a") as log:
    log.write(f"\n--- REAL SCAN {target} pada {datetime.datetime.now()} ---\n")
    
    for p in ports_list:
        port = int(p.strip())
        
        # buat socket baru
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # tunggu 1 saat je
        
        result = s.connect_ex((target, port))
        s.close()
        
        if result == 0:
            status = "OPEN"
        else:
            status = "CLOSED"
        
        print(f"Port {port} {status}")
        log.write(f"Port {port} {status}\n")

print("Scan siap. Log disimpan.")
print("\n--- ISI LOG ---")
print(open("scan.log").read())