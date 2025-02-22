#cau9:
x, y, z = map(float, input("Nhập tọa độ điểm: ").split())
print("Qua Oxy:", (x, y, -z))
print("Qua Oxz:", (x, -y, z))
print("Qua Oyz:", (-x, y, z))