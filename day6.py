open_ports = [22, 443, 3389]

ports_input = input("Taip port nak scan (contoh: 22,80,443): ")

ports_list = ports_input.split(",")

for p in ports_list:
    port = int(p)
    if port in open_ports:
        print(f"Port {port} OPEN")
    else:
        print(f"Port {port} CLOSED")