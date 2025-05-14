import Matranvuong

n = int(input("Nhap kich thuoc: "))
matran = Matranvuong.nhap_ma_tran(n)

print("ma tran:")
Matranvuong.in_ma_tran(matran)

print("Ma tran chuyen vi:")
Matranvuong.in_ma_tran(Matranvuong.chuyen_vi(matran))

if Matranvuong.doi_xung(matran):
    print("ma tran doi xung")
else:
    print("Ma tran khong doi xung")