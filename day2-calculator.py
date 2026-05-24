# Day 2 - Kalkulator Simple
print("=== KALKULATOR PYTHON ===")

a = float(input("Nombor 1: "))
b = float(input("Nombor 2: "))
op = input("Pilih (+, -, *, /): ")

if op == "+":
    print(f"Hasil: {a+b}")
elif op == "-":
    print(f"Hasil: {a-b}")
elif op == "*":
    print(f"Hasil: {a*b}")
elif op == "/":
    if b != 0:
        print(f"Hasil: {a/b}")
    else:
        print("Error: bahagi 0")
else:
    print("Operasi tak sah")

print("\nDibuat oleh shah77-ctrl - Day 2")

