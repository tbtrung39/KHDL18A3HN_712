import matranvuong 
N = int(input("Hay nhap kich thuoc ma tran can tinh: "))
ma_tran = matranvuong.nhap_ma_tran(N)

print("Ma tran da nhap la:")
matranvuong.in_ma_tran(ma_tran)

chuyen_vi = matranvuong.ma_tran_chuyen_vi(ma_tran)
print("Ma tran chuyen vi:")
matranvuong.in_ma_tran(chuyen_vi)

if matranvuong.kiem_tra_doi_xung(ma_tran):
    print("Ma tran la doi xung.")
else:
    print("Ma tran khong phai doi xung.")