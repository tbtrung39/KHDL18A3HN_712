import my_Triange 
a = float(input("Nhap canh a: "))
b = float(input("Nhap canh b: "))
c = float(input("Nhap canh c: "))
if my_Triange.is_TamGiac(a, b, c):
    print("Day la mot tam giac.")
    print("Chu vi tam giac la:", my_Triange.ChuviTamGiac(a, b, c))
    print("Dien tich tam giac la:", my_Triange.S_TamGiac(a, b, c))
else:
    print("Ba canh da nhap khong tao thanh mot tam giac")