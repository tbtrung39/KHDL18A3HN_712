from hinhhoc.my_Triange import chu_vi_tam_giac, dien_tich_tam_giac, check_tam_giac
from hinhhoc.my_square import chu_vi_hinh_vuong, dien_tich_hinh_vuong

print("=== TÍNH TOÁN HÌNH HỌC ===")
print("1. Tính tam giác")
print("2. Tính hình vuông")
chon = input("Nhập lựa chọn (1 hoặc 2): ")

if chon == "1":
    print("Nhập độ dài 3 cạnh tam giác:")
    a = float(input("Cạnh a: "))
    b = float(input("Cạnh b: "))
    c = float(input("Cạnh c: "))
    chu_vi = chu_vi_tam_giac(a, b, c)
    dien_tich = dien_tich_tam_giac(a, b, c)
    if chu_vi is not None and dien_tich is not None:
        print(f"Chu vi tam giác: {chu_vi}")
        print(f"Diện tích tam giác: {dien_tich}")
        kiem_tra = check_tam_giac(a, b, c)
        print(f"==> Ba số {a}, {b}, {c} có tạo thanh một tam giác không?")
        print("True" if kiem_tra else "False")
    else:
        print("Cạnh tam giác phải là số dương.")
elif chon == "2":
    canh = float(input("Nhập cạnh hình vuông: "))
    chu_vi = chu_vi_hinh_vuong(canh)
    dien_tich = dien_tich_hinh_vuong(canh)
    if chu_vi is not None and dien_tich is not None:
        print(f"Chu vi hình vuông: {chu_vi}")
        print(f"Diện tích hình vuông: {dien_tich}")
    else:
        print("Cạnh hình vuông phải là số dương.")
else:
    print("Lựa chọn không hợp lệ.")

