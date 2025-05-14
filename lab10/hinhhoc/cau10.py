import my_Triange   
a = float(input("hay nhap canh  a: "))
b = float(input("hay nhap canh  b: "))
c = float(input("hay nhap canh c: "))
if my_Triange.is_TamGiac(a, b, c):
    print("day la mot tam giac.")
    print("Chu vi tam giac la:", my_Triange.ChuviTamGiac(a, b, c))
    print("s tam giac la:", my_Triange.S_TamGiac(a, b, c))
else:
    print("Ba canh da nhap ko tao thanh mot tam giac")

import my_square 
a = float(input("hay nhap canh hinh vuong: "))

chu_vi = my_square.ChuviHinhVuong(a)
dien_tich = my_square.DientichHinhVuong(a)

print("Chu vi hinh vuong la:", chu_vi)
print("dien tich hvuong la:", dien_tich)