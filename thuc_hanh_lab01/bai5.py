# Nhập vectơ a
chuoi_a = input("Nhập vectơ a (các số cách nhau bởi dấu cách): ")
a = list(map(float, chuoi_a.split()))

# Nhập vectơ b
chuoi_b = input("Nhập vectơ b (các số cách nhau bởi dấu cách): ")
b = list(map(float, chuoi_b.split()))

# Tính tích vô hướng
tich_vo_huong = 0
for i in range(len(a)):
  tich_vo_huong += a[i] * b[i]

# In kết quả
print("Tích vô hướng của a và b là:", tich_vo_huong)
