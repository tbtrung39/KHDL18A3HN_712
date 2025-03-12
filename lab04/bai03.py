import math
x=float(input("Nhập giá trị x (đơn vị radian): "))  
cos_x=1 
n=0  
gia_tri=1  
while True:
    n+=1  
    gia_tri*=-(x**2)/((2*n-1)*(2*n))  
    cos_x+=gia_tri 
    if abs(cos_x-math.cos(x))<10**(-4): 
        break
print(f"Giá trị xấp xỉ của cos({x}): {cos_x:.6f}")  
print(f"Giá trị thực của cos({x}): {math.cos(x):.6f}")  
print(f"Sai số cuối cùng: {abs(cos_x-math.cos(x)):.6f}")  