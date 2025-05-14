from hinhhoc import my_Triage, my_square
print("Tam giác:")
a, b, c = map(float, input("Nhập 3 cạnh: ").split())
if my_Triage.is_TamGiac(a, b, c):
    print("Chu vi:", my_Triage.ChuviTamGiac(a, b, c))
    print("Diện tích:", my_Triage.S_TamGiac(a, b, c))
else:
    print("Không phải tam giác.")
print("Hình vuông:")
a = float(input("Nhập cạnh hình vuông: "))
print("Chu vi:", my_square.ChuviHinhvuong(a))
print("Diện tích:", my_square.Dien_tich_hinh_vuong(a))
