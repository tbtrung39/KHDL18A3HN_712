n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Nhập lại n (n > 0): "))
tong = 0
for i in range(1, n + 1):
    tong += 1 / i
print("Tổng nghịch đảo:", round(tong, 6))
