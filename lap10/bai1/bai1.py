import my_triange
a=int(input("nhap a: "))
b=int(input("nhap b: "))
c=int(input("nhap c: "))
if my_triange.is_TamGiac(a,b,c):
    print("ba canh tao thanh mot tam giac")
    print("chu vi tam giac",my_triange.ChuviTamGiac(a,b,c))
    print("dien tich hinh tam giac:",my_triange.S_TamGiac(a,b,c))
else:
    print("ba canh khong tao thanh mot tam giac")