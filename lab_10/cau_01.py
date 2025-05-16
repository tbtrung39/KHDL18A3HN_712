import my_Triange

print("=== KIỂM TRA TAM GIÁC ===")
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
chu_vi = my_Triange.chu_vi_tam_giac(a, b, c)
dien_tich = my_Triange.dien_tich_tam_giac(a, b, c)
if chu_vi is not None and dien_tich is not None:
    print(f"Chu vi tam giác: {chu_vi}")
    print(f"Diện tích tam giác: {dien_tich}")
    kiem_tra = my_Triange.check_tam_giac(a, b, c)
    print(f"==> Ba số {a}, {b}, {c} có tạo thanh một tam giác không?")
    print("True" if kiem_tra else "False")
else:
    print("Cạnh tam giác phải là số dương.")
