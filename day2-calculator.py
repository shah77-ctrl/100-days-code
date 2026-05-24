# Day 2 - Kalkulator Simple
print("=== KALKULATOR PYTHON ===")

a = float(input("Nombor 1: "))
b = float(input("Nombor 2: "))
op = input("Pilih (+, -, *, /): ")

if op == "+": print(f"Hasil: {a+b}")
elif op == "-": print(f"Hasil: {a-b}")
elif op == "*": print(f"Hasil: {a*b}")
elif op == "/": print(f"Hasil: {a/b}" if b != 0 else "Error: bahagi 0")
else: print("Operasi tak sah")
