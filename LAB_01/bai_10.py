import math
x=float(input("nhập giá trị của x:"))
log4_x = math.log(x)/math.log(4)
log8_x = math.log(x)/math.log(8)
S=log4_x + log8_x
print(f"Giá trị của S là: {S:.4f}")