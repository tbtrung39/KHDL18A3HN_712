n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    print("Vui lòng nhập số nguyên dương lớn hơn 0!")
    n = int(input("Nhập lại số nguyên dương n: "))
S5 = 0
for i in range(n):
    So_le = 2 * i + 1
    S5 += So_le ** 3
print(f"Tổng S5 = 1**3 + 3**3 + 5**3 + ... + (2n+1)**3 là: {S5}")
