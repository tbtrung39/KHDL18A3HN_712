x1, y1, z1 = map(float, input("Nhập tọa độ vector a (x y z): ").split())
x2, y2, z2 = map(float, input("Nhập tọa độ vector b (x y z): ").split())

tich_vo_huong = x1*x2 + y1*y2 + z1*z2

print(f"Tích vô hướng của hai vector: {tich_vo_huong}")