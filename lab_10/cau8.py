import matranvuong 
N = int(input("hay nhap kich thuoc ma trajn can tinh: "))
ma_tran = matranvuong.nhap_ma_tran(N)

print("\nma tran da nhap la:")
matranvuong.in_ma_tran(ma_tran)

chuyen_vi = matranvuong.ma_tran_chuyen_vi(ma_tran)
print("\nma tran chuyen vi:")
matranvuong.in_ma_tran(chuyen_vi)

if matranvuong.kiem_tra_doi_xung(ma_tran):
    print("\nma tran la doi xung.")
else:
    print("\nma tran khong phai doi xung.")