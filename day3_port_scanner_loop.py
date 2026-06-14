ports = [22, 80, 443, 8080]
open_ports = [80, 8080]

for port in ports:
    if port in open_ports:
        print(f"Port {port} : OPEN - perlu audit!")
    else:
        print(f"Port {port} : closed")