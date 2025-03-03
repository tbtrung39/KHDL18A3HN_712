import math
r = float(input("Nhập bán kính của khối trụ là: "))
h = float(input("Nhập chiều cao của khối trụ là: "))
S = 1
pi = 3.14
S_xung_quanh =2 * pi * r * h
S_toan_phan = 2 * pi * r * (r + h)
V = pi * r**2 * h
S_xung_quanh = round(S_xung_quanh, 2)
S_toan_phan = round(S_toan_phan, 2)
V = round(V, 2)
print(f"Diện tích xung quanh: {S_xung_quanh}")
print(f"Diện tích toàn phần: {S_toan_phan}")
print(f"Thể tích khối trụ: {V}")