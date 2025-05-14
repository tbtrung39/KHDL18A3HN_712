import matranvuong

N = int(input("Nhập kích thước ma trận NxN: "))
matran = matranvuong.nhap_matran(N)

print("Ma trận vừa nhập:")
matranvuong.in_matran(matran)

print("Ma trận chuyển vị:")
matranvuong.in_matran(matranvuong.chuyen_vi(matran))

if matranvuong.kiem_tra_doi_xung(matran):
    print("Ma trận đối xứng.")
else:
    print("Ma trận không đối xứng.")