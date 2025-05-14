import my_Triange 
a = float(input("Hay nhap canh  a: "))
b = float(input("Hay nhap canh  b: "))
c = float(input("Hay nhap canh c: "))
if my_Triange.is_TamGiac(a, b, c):
    print("Day la mot tam giac.")
    print("Chu vi tam giac la:", my_Triange.ChuviTamGiac(a, b, c))
    print("Dien tich tam giac la:", my_Triange.S_TamGiac(a, b, c))
else:
    print("Ba canh da nhap khong tao thanh mot tam giac")