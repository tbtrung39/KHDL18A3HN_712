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

import my_square 
a = float(input("Hay nhap canh hinh vuong: "))

chu_vi = my_square.ChuviHinhVuong(a)
dien_tich = my_square.DientichHinhVuong(a)

print("Chu vi hinh vuong la:", chu_vi)
print("Dien tich hinh vuong la:", dien_tich)