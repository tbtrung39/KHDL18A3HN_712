while True:
    n = int(input("Nhap n nguyen duong: "))
    if n > 0:
        break
    print("n phai la so nguyen duong. Vui long nhap lai!")

S4 = 0
for i in range(1, n + 1):
    S4 += i ** 2
print(f"a) S4 = {S4}")

S5 = 0
for i in range(n + 1):
    S5 += (2*i + 1) ** 3
print(f"b) S5 = {S5}")

S6 = 0
for i in range(1, n + 1):
    S6 += (2*i) ** 4
print(f"c) S6 = {S6}")
