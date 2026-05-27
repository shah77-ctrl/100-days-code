ports = [22, 80, 443, 8080]
open_ports = [22, 443]

log = open("scan_log.txt", "w")

for port in ports:
    if port in open_ports:
        hasil = f"port {port} : OPEN - perlu audit!"
    else:
        hasil = f"port {port} : closed"
        
    print(hasil)
    log.write(hasil + "\n") 
    
log.close()
print("log siap disimpan!")