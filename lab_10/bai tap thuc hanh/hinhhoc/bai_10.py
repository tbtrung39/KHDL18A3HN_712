import my_square

canh = float(input("Nhập độ dài cạnh hình vuông: "))

chu_vi = my_square.ChuViHinhVuong(canh)
dien_tich = my_square.Dien_tich_hinh_vuong(canh)

print(f"Chu vi hình vuông: {chu_vi}")
print(f"Diện tích hình vuông: {dien_tich}")

import my_triangle
a,b,c=3,4,5

if my_triangle.is_Tamgiac(a,b,c):
    print("Ba cạnh tạo thành một tam giác.")
    print("Chu vi tam giác:",my_triangle.Chu_vi_tam_giac(a,b,c))
    print("Diện tích tam giác:",my_triangle.Dien_tich_tam_giac(a,b,c))
else:
    print("Ba cạnh không tạo thành một tam giác.")