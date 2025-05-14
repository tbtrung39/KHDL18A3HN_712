from pkg import Matranvuong

n = int(input("Nhập kích thước ma trận vuông N: "))
matran = Matranvuong.nhap_ma_tran(n)

print("Ma trận:")
Matranvuong.in_ma_tran(matran)

print("Ma trận chuyển vị:")
Matranvuong.in_ma_tran(Matranvuong.chuyen_vi(matran))

if Matranvuong.doi_xung(matran):
    print("Ma trận đối xứng.")
else:
    print("Ma trận không đối xứng.")
