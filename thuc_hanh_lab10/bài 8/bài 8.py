import Matranvuong

N = int(input("Nhập kích thước ma trận NxN: "))
matran = Matranvuong.nhap_matran(N)
print("Ma trận vừa nhập:")
Matranvuong.in_matran(matran)
print("Ma trận chuyển vị:")
Matranvuong.in_matran(Matranvuong.chuyen_vi(matran))
if Matranvuong.kiem_tra_doi_xung(matran):
    print("Ma trận đối xứng.")
else:
    print("Ma trận không đối xứng.")