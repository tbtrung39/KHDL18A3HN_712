from pkg import my_square

canh = float(input("Nhập độ dài cạnh hình vuông: "))

chu_vi = my_square.ChuViHinhVuong(canh)
dien_tich = my_square.Dien_tich_hinh_vuong(canh)

print(f"Chu vi hình vuông: {chu_vi}")
print(f"Diện tích hình vuông: {dien_tich}")
