import Matranvuong 
N = int(input("hay nhap kich thuoc ma trajn can tinh: "))
ma_tran = Matranvuong.nhap_ma_tran(N)

print("\nma tran da nhap la:")
Matranvuong.in_ma_tran(ma_tran)

chuyen_vi = Matranvuong.ma_tran_chuyen_vi(ma_tran)
print("\nma tran chuyen vi:")
Matranvuong.in_ma_tran(chuyen_vi)

if Matranvuong.kiem_tra_doi_xung(ma_tran):
    print("\nma tran la doi xung.")
else:
    print("\nma tran khong phai doi xung.")