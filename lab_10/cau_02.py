import my_square

print("=== TÍNH TOÁN HÌNH VUÔNG ===")
a = float(input("Nhập độ dài cạnh hình vuông: "))
chu_vi = my_square.chu_vi_hinh_vuong(a)
dien_tich = my_square.dien_tich_hinh_vuong(a)
if chu_vi is not None and dien_tich is not None:
    print(f"Chu vi hình vuông: {chu_vi}")
    print(f"Diện tích hình vuông: {dien_tich}")
else:
    print("Cạnh hình vuông phải lớn hơn 0.")
