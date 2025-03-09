so = int(input("Nhập số: "))
tong = 0

while so > 0:
    tong += so % 10
    so //= 10

print("Tổng các chữ số:", tong)