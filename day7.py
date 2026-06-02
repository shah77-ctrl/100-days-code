import datetime

open_ports = [22, 443, 3389]

target = input("Target IP: ")
ports_input = input("Port nak scan (contoh: 22,80,443): ")
ports_list = ports_input.split(",")

# buka file untuk tulis
log = open("scan.log", "a")

log.write(f"\n--- Scan {target} pada {datetime.datetime.now()} ---\n")

for p in ports_list:
    port = int(p.strip())  # .strip() buang space
    if port in open_ports:
        status = "OPEN"
    else:
        status = "CLOSED"
    
    print(f"Port {port} {status}")
    log.write(f"Port {port} {status}\n")

log.close()
print("Log disimpan ke scan.log")

print("\n--- ISI LOG ---")
print(open("scan.log").read())