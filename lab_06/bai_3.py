danh_sach = []
while True:
    so = int(input("Nhap so tu nhien (nhap 0 de ket thuc): "))
    if so == 0:
        break
    danh_sach.append(so)

duong = [x for x in danh_sach if x > 0]
am_va_khong = [x for x in danh_sach if x <= 0]
danh_sach_moi = duong + am_va_khong

print("Danh sach sau khi sap xep:")
print(danh_sach_moi)
m = int(input("\nNhap so m can them: "))
danh_sach_moi.insert(0, m)
danh_sach_moi.append(m)

if len(danh_sach_moi) >= 5:
    danh_sach_moi.insert(4, m)
print("\nDanh sach sau khi chen m:")
print(danh_sach_moi)
