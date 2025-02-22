# Bài 12: 
import math 
t=float(input("Nhập thời gian t:")) 
a=float(input("Nhập giá trị a:")) 
v=-t*(math.log(5,4)) + a**4 
print(f"Giá trị của biểu thức là: {v:0.2f}")