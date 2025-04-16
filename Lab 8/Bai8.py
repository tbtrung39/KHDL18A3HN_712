#Bai8
import math
def tinh_chu_vi(r):
    return 2 * math.pi * r
def tinh_dien_tich(r):
    return math.pi * r**2
r = float(input("Nhập bán kính: "))
print("Chu vi hình tròn là:", tinh_chu_vi(r))
print("Diện tích hình tròn là:", tinh_dien_tich(r))