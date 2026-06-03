import datetime
import socket

# database ringkas port biasa
services = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 443: "HTTPS",
    3306: "MySQL", 3389: "RDP"
}

target = input("Target IP: ")
start = int(input("Port mula: "))
end = int(input("Port akhir: "))

print(f"\nScanning {target} {start}-{end}...\n")

with open("scan.log", "a") as log:
    log.write(f"\n--- SERVICE SCAN {target} pada {datetime.datetime.now()} ---\n")
    
    for port in range(start, end + 1):
        s = socket.socket()
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        s.close()
        
        if result == 0:
            service = services.get(port, "Unknown")
            print(f"Port {port} OPEN - {service}")
            log.write(f"Port {port} OPEN - {service}\n")

print("\nSelesai.")