n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Vui lòng nhập n > 0: "))
S4 = 0
S5 = 0
S6 = 0
for i in range(1, n+1):
    S4 += i**2
for i in range(n):
    S5 += (2*i+1)**3
for i in range(1, n+1):
    S6 += (2*i)**4
print("S4 =", S4)
print("S5 =", S5)
print("S6 =", S6)
