#Bai7
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
delta = b**2 - 4*a*c
x_dinh= -b / (2*a)
y_dinh= -delta / (4*a)
print(f"Tọa độ đỉnh của parabol: ({x_dinh:0.2f}, {y_dinh:0.2f})")