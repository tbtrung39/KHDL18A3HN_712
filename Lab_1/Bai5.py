#Bai5
a1, a2 = map(float, input("Nhập tọa độ của vector a: ").split())
b1, b2 = map(float, input("Nhập tọa độ của vector b: ").split())
tich_vo_huong = a1 * b1 + a2 * b2
print("Tích vô hướng của 2 vector vừa nhập là: %0.2f" % tich_vo_huong)