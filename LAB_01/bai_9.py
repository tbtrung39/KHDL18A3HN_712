x = float(input("Nhập tọa độ x: "))
y = float(input("Nhập tọa độ y: "))
z = float(input("Nhập tọa độ z: "))
Oxy = (x, y, -z)
Oxz = (x, -y, z)
Oyz = (-x, y, z)
print("Tọa độ điểm đối xứng qua mặt phẳng Oxy:", Oxy)
print("Tọa độ điểm đối xứng qua mặt phẳng Oxz:", Oxz)
print("Tọa độ điểm đối xứng qua mặt phẳng Oyz:", Oyz)