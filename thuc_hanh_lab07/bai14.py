tu_dien = {}
for i in range(1, 101):
    n = i
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    tu_dien[i] = binary
for key, value in tu_dien.items():
    print(", ".join([f"({key}, '{value}')" for key, value in tu_dien.items()]))