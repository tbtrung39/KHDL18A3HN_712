#cau7:
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
x_dinh = -b / (2 * a)
y_dinh = - (b**2 - 4*a*c) / (4*a)
print("Tọa độ đỉnh: (", round(x_dinh, 2), ",", round(y_dinh, 2), ")")