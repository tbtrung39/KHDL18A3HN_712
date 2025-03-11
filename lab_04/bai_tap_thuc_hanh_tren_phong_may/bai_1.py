while True:
    n = int(input("Nhập số nguyên dương n: "))
    if n > 0:
        break
    print("Vui lòng nhập lại số nguyên dương!")

# Tính tổng S4 
S4 = 0
i = 1
while i <= n:
    S4 += i ** 2
    i += 1
print("Tổng S4 =", S4)
# Tính tổng S5 
S5 = 0
i = 1
while i <= (2 * n + 1):
    S5 += i ** 3
    i += 2
print("Tổng S5 =", S5)
# Tính tổng S6 
S6 = 0
i = 2
while i <= (2 * n):
    S6 += i ** 4
    i += 2
print("Tổng S6 =", S6)
