#Bai3
import math

r = float(input("Nhập bán kính của hình trụ (r): "))
h = float(input("Nhập chiều cao của hình trụ (h): "))

s_xq = 2 * math.pi * r * h
s_tp = 2 * math.pi * r * (r + h)
v = math.pi * r**2 * h

print("Diện tích xung quanh của hình trụ là:", s_xq)
print("Diện tích toàn phần của hình trụ là:", s_tp)
print("Thể tích của hình trụ là:", v)