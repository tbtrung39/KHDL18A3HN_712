import matranvuong
N = int(input("Nhap kich thuoc N (ma tran NxN): "))
A = matranvuong.nhap_matran(N)
print("\nMa tran vua nhap:")
matranvuong.in_matran(A)
CT = matranvuong.chuyen_vi(A)
print("\nMa tran chuyen vi:")
matranvuong.in_matran(CT)
if matranvuong.kiem_tra_doi_xung(A):
    print("\nMa tran doi xung")
else:
    print("\nMa tran khong doi xung")
