from hinhhoc import my_Triange, my_square
a = float(input("Nhap canh hinh vuong: "))
print("→ Chu vi hinh vuong:", my_square.ChuViHinhvuong(a))
print("→ Dien tich hinh vuong:", my_square.Dien_tich_hinh_vuong(a))
a = float(input("Nhap canh a cua tam giac: "))
b = float(input("Nhap canh b cua tam giac: "))
c = float(input("Nhap canh c cua tam giac: "))
if my_Triange.is_TamGiac(a, b, c):
    print("Chu vi tam giac:", my_Triange.ChuViTamGiac(a, b, c))
    print("Dien tich tam giac:", my_Triange.S_TamGiac(a, b, c))
else:
    print("Ba canh khong tao thanh tam giac.")