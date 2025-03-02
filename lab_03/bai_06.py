n = int(input("Nhập n: "))
tong = 0
for i in range(1, n + 1):
    tong += i ** 3
print(f"Tổng lập phương của {n} số nguyên đầu tiên là: {tong}")