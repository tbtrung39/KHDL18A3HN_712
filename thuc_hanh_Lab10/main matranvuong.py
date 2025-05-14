import Matranvuong
n = int(input("Nhập kích thước ma trận vuông N: "))
matran = Matranvuong.nhap_ma_tran(n)
print("\n--- In ma trận ---")
Matranvuong.in_ma_tran(matran)
print("\n--- Ma trận chuyển vị ---")
matran_chuyen_vi = Matranvuong.chuyen_vi(matran)
Matranvuong.in_ma_tran(matran_chuyen_vi)
print("\n--- Kiểm tra đối xứng ---")
if Matranvuong.la_ma_tran_doi_xung(matran):
    print("Ma trận đối xứng: True")
else:
    print("Ma trận không đối xứng: False")
