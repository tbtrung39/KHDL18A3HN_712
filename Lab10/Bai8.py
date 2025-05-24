import Matranvuong
n = int(input("Nhap kich thuoc ma tran N x N: "))
matran = Matranvuong.nhap_ma_tran(n)
print("Tong cac phan tu trong ma tran:", Matranvuong.tinh_tong(matran))
if Matranvuong.kiem_tra_doi_xung(matran):
    print("Ma tran doi xung.")
else:
    print("Ma tran khong doi xung.")