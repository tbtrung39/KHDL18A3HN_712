import Matranvuong

print("=== CHƯƠNG TRÌNH MA TRẬN N X N ===")

N = int(input("Nhập kích thước ma trận N (NxN): "))
ma_tran = Matranvuong.nhap_ma_tran(N)
print("\nMa trận đã nhập:")
Matranvuong.in_ma_tran(ma_tran)
ma_tran_chuyen_vi = Matranvuong.ma_tran_chuyen_vi(ma_tran)
print("\nMa trận chuyển vị:")
Matranvuong.in_ma_tran(ma_tran_chuyen_vi)

doi_xung = Matranvuong.kiem_tra_doi_xung(ma_tran)
print("\n==> Ma trận có đối xứng không?")
print("True" if doi_xung else "False")
