import Matranvuong 

n = int(input("Hay nhap kich thuoc ma tran can tinh: "))
ma_tran = Matranvuong.nhap_ma_tran(n)

print("Ma tran da nhap la:")
Matranvuong.in_ma_tran(ma_tran)

chuyen_vi = Matranvuong.ma_tran_chuyen_vi(ma_tran)
print("Ma tran chuyen vi:")
Matranvuong.in_ma_tran(chuyen_vi)

if Matranvuong.kiem_tra_doi_xung(ma_tran):
    print("Ma tran la doi xung.")
else:
    print("Ma tran khong phai doi xung.")