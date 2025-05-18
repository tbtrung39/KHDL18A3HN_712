import my_square
a = int(input("Nhập cạnh của hình vuông là: "))
chu_vi_hinh_vuong = my_square.Chuvihinhvuong(a)
dien_tich_hinh_vuong = my_square.Dientichhinhvuong(a)
print(f"Chu vi của hình vuông là: {chu_vi_hinh_vuong}")
print(f"Diện tích hình vuông là:{dien_tich_hinh_vuong}")