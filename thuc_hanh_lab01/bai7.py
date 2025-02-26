# Nhập hệ số của phương trình bậc 2
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

# Tính tọa độ đỉnh của phương trình bậc 2
x_dinh = -b / (2 * a)
y_dinh = - (b**2 - 4*a*c) / (4 * a)

# In kết quả (làm tròn đến 2 chữ số thập phân)
print("Tọa độ đỉnh của phương trình bậc 2 là: ({:.2f}, {:.2f})".format(x_dinh, y_dinh))
