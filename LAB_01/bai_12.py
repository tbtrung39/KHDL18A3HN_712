import math
x = float(input("nhập giá trị a: "))
log4_5= math.log(5)/math.log(4)
t = -(x**4)/ log4_5
print(f"Giá trị của t là: {t:.4f}")