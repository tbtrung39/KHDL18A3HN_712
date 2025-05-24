from hinhhoc import is_TamGiac, ChuViTamGiac, S_TamGiac, ChuViHinhVuong, Dien_tich_hinh_vuong

a,b,c = map(float, input("Nhập 3 cạnh tam giác a,b,c: ").split())
print("Kiểm tra tam giác:", is_TamGiac(a,b,c))
if is_TamGiac(a,b,c):
    print("Chu vi tam giác:", ChuViTamGiac(a,b,c))
    print("Diện tích tam giác:", S_TamGiac(a,b,c))
else:
    print("Không phải tam giác")

a = float(input("Nhập cạnh hình vuông a: "))
print("Chu vi hình vuông:", ChuViHinhVuong(a))
print("Diện tích hình vuông:", Dien_tich_hinh_vuong(a))
