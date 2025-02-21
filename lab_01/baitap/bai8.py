x1, y1 = map(float, input("Nhập tọa độ A: ").split())
x2, y2 = map(float, input("Nhập tọa độ B: ").split())
x3, y3 = map(float, input("Nhập tọa độ C: ").split())
x_g = (x1 + x2 + x3) / 3
y_g = (y1 + y2 + y3) / 3
print("Tọa độ trọng tâm: (", round(x_g, 2), ",", round(y_g, 2), ")")