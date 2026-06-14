print("=== Scanner Interakrtid Day 5 ===")

port_input = input("Taip port nak scan (contoh: 22):  ")

port = int(port_input)

open_ports = (22, 443)

if port in open_ports:
    hasil = f"port {port} : open - perlu audit!"
else:
    hasil = f"port {port} :closed"
    
print(hasil)

log = open("scan_log.txt", "a")
log.write(hasil+"\n")
log.close()

print("log ditambah!")