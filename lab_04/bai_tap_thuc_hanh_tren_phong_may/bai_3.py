import math

x = float(input("Nhập giá trị x (radian): "))

so_hang_dau = 1  
cos_x = so_hang_dau  
n = 1  

while abs(so_hang_dau) >= 1e-4:
    so_hang_dau *= -x**2 / (2 * n * (2 * n - 1))  
    cos_x += so_hang_dau
    n += 1  

print(f"Giá trị gần đúng của cos({x}) là: {cos_x}")