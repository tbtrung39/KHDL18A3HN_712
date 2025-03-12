#Bai3
x = float(input("Nhập x: "))
cos_x = 1  
so_hang_dau = 1   
n = 1      
while True:
    so_hang_dau = -so_hang_dau * (x**2) / ((2*n - 1) * (2*n))  
    cos_x += so_hang_dau
    if abs(so_hang_dau) < 10**-4:  
        break
    n += 1  
print("Giá trị xấp xỉ của cos(", x, ") =", cos_x)