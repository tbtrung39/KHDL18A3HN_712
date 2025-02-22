#cau3:
r = float(input("Nhập bán kính: "))
h = float(input("Nhập chiều cao: "))
pi = 3.14
s_xq = 2 * pi * r * h
s_tp = 2 * pi * r * (r + h)
v = pi * r**2 * h
print("Diện tích xung quanh:", round(s_xq, 2))
print("Diện tích toàn phần:", round(s_tp, 2))
print("Thể tích:", round(v, 2))