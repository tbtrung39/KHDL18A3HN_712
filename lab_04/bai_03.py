x = float(input("Nhap x: "))
sai_so = 1e-4
cos_x = 1
so_hang = 1
n = 1

while abs(so_hang) > sai_so:
    so_hang = so_hang * (-x**2) / (2*n*(2*n-1))
    cos_x += so_hang
    n += 1
print(f"cos({x}) = {cos_x}")