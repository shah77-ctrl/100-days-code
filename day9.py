import datetime
import socket

target = input("Target IP: ")
start = int(input("Port mula: "))
end = int(input("Port akhir: "))

print(f"\nScanning {target} dari {start} ke {end}...\n")

open_found = []

with open("scan.log", "a") as log:
    log.write(f"\n--- RANGE SCAN {target} {start}-{end} pada {datetime.datetime.now()} ---\n")
    
    for port in range(start, end + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)  # laju sikit
        
        result = s.connect_ex((target, port))
        s.close()
        
        if result == 0:
            print(f"Port {port} OPEN")
            log.write(f"Port {port} OPEN\n")
            open_found.append(port)

print(f"\nSelesai. Jumpa {len(open_found)} port buka.")
print("\n--- ISI LOG TERKINI ---")
with open("scan.log", "r") as f:
    print(f.read()[-500:])  # tunjuk 500 huruf terakhir je
