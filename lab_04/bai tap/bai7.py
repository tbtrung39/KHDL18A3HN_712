a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))

x = a
y = b

# Tìm ước chung lớn nhất (ƯCLN) bằng vòng lặp
while y != 0:
    tam = y
    y = x % y
    x = tam

ucln = x
bcnn = (a * b) // ucln  # Tính BCNN

print("Bội chung nhỏ nhất là:", bcnn)
