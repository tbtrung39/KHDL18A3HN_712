from pkg import matranvuong

n = int(input("Nhập kích thước ma trận vuông N: "))
mat = matranvuong.nhap_ma_tran(n)

matranvuong.in_ma_tran(mat)

print("\nMa trận chuyển vị:")
transposed = matranvuong.chuyen_vi(mat)
matranvuong.in_ma_tran(transposed)

print("\nMa trận có đối xứng không?")
print(matranvuong.kiem_tra_doi_xung(mat))
