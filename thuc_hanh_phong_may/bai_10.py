import math
x = float(input("Nhập giá trị x: "))
log4_x = math.log(x, 4)
logx_2 = math.log(2, x)
bieuthuc = log4_x + logx_2
print(f"f({x}) = {round(bieuthuc, 2)}")
