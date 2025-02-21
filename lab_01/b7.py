# bài 7
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
toado_x = -b / (2 * a)
toado_y= (4 * a * c - b**2) / (4 * a)
toado_x = round(toado_x, 2)
toado_y = round(toado_y, 2)
print(f"Tọa độ đỉnh của parabol: ({toado_x}, {toado_y})")
