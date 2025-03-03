import math
x = float(input("Nhập giá trị x: "))
print(f"Giá trị x đã nhập: {x}")
if x > 0 and x != 1:
    fx = (math.log(x) / math.log(4)) + (math.log(2) / math.log(x))  
    print(f"Giá trị của f(x) là: {fx:.2f}")  
else:
    print("Nhập lại.")
