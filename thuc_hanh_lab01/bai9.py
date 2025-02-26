# Nhập tọa độ điểm trong không gian Oxyz
x = float(input("Nhập x: "))
y = float(input("Nhập y: "))
z = float(input("Nhập z: "))

# Tính tọa độ điểm đối xứng qua mặt phẳng Oxy
x_oxy = x
y_oxy = y
z_oxy = -z

# Tính tọa độ điểm đối xứng qua mặt phẳng Oxz
x_oxz = x
y_oxz = -y
z_oxz = z

# Tính tọa độ điểm đối xứng qua mặt phẳng Oyz
x_oyz = -x
y_oyz = y
z_oyz = z

# In kết quả
print("Tọa độ điểm đối xứng qua mặt phẳng Oxy là: ({}, {}, {})".format(x_oxy, y_oxy, z_oxy))
print("Tọa độ điểm đối xứng qua mặt phẳng Oxz là: ({}, {}, {})".format(x_oxz, y_oxz, z_oxz))
print("Tọa độ điểm đối xứng qua mặt phẳng Oyz là: ({}, {}, {})".format(x_oyz, y_oyz, z_oyz))
