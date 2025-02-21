# Bài 10: 
import math
x = float(input("Nhập giá trị x: "))
fx = (math.log(x) / math.log(4)) + (math.log(2) / math.log(x))
fx = round(fx, 2) # Bài 8:
xA, yA = map(float, input("Nhập tọa độ A (xA yA): ").split())
xB, yB = map(float, input("Nhập tọa độ B (xB yB): ").split())
xC, yC = map(float, input("Nhập tọa độ C (xC yC): ").split())
#  gọi G là trọng tâm của tam giác ABC đã cho 
xG = (xA + xB + xC) / 3
yG = (yA + yB + yC) / 3
xG = round(xG, 2)
yG = round(yG, 2)
print("Tọa độ trọng tâm của tam giác là:", (xG, yG))
 # làm tròn
print("Giá trị của biểu thức đã cho là:", fx)
