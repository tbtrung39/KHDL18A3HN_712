import math
x=int(input("nhập giá trị x(x>1): ")) 
if x<=1: 
    print("nhập giá trị x không đúng yêu cầu, vui lòng nhập lại") 
else:
    f=round(math.log(4,x) + math.log(x,2),2) 
    print("giá trị biểu thức f(x) là",f) 
