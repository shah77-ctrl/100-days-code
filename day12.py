import socket
import datetime
from concurrent.futures import ThreadPoolExecutor

services = {
    21:"FTP",22:"SSH",23:"Telnet",25:"SMTP",53:"DNS",
    80:"HTTP",110:"POP3",143:"IMAP",443:"HTTPS",
    3306:"MySQL",3389:"RDP",8080:"HTTP-Alt"
}

target = input("Target IP: ")
start = int(input("Port mula: "))
end = int(input("Port akhir: "))

print(f"\n[FAST SERVICE SCAN] {target} {start}-{end}\n")
start_time = datetime.datetime.now()

def scan(port):
    s = socket.socket()
    s.settimeout(0.5)
    res = s.connect_ex((target, port))
    s.close()
    if res == 0:
        return (port, services.get(port, "Unknown"))
    return None

open_list = []
with ThreadPoolExecutor(max_workers=100) as ex:
    for result in ex.map(scan, range(start, end+1)):
        if result:
            port, svc = result
            print(f"Port {port} OPEN - {svc}")
            open_list.append(result)

duration = (datetime.datetime.now() - start_time).total_seconds()

with open("scan.log","a") as log:
    log.write(f"\n--- DAY12 {target} {start}-{end} {datetime.datetime.now()} ({duration:.2f}s) ---\n")
    for p,s in open_list:
        log.write(f"{p}/{s}\n")

print(f"\nSelesai dalam {duration:.2f} saat. Jumpa {len(open_list)} port.")