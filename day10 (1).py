import socket
import datetime
from concurrent.futures import ThreadPoolExecutor

target = input("Target IP: ")
start = int(input("Port mula: "))
end = int(input("Port akhir: "))

print(f"\nFast scan {target} {start}-{end}...\n")

open_ports = []

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    s.close()
    if result == 0:
        print(f"Port {port} OPEN")
        return port
    return None

with ThreadPoolExecutor(max_workers=100) as executor:
    results = executor.map(scan_port, range(start, end + 1))
    open_ports = [p for p in results if p]

with open("scan.log", "a") as log:
    log.write(f"\n--- FAST SCAN {target} {start}-{end} pada {datetime.datetime.now()} ---\n")
    for p in open_ports:
        log.write(f"Port {p} OPEN\n")

print(f"\nSelesai. Jumpa {len(open_ports)} port buka.")