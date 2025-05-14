from sinhngaunhien import sinh_ngau_nhien, tong_cac_so_le, so_nguyen_to_chia_het_cho_7, so_chinh_phuong
ngau_nhien = sinh_ngau_nhien()
print("Dãy số ngẫu nhiên:", ngau_nhien)
tong_le = tong_cac_so_le(ngau_nhien)
print("Tổng các số lẻ:", tong_le)
so_nguyen_to_7 = so_nguyen_to_chia_het_cho_7(ngau_nhien)
print("Các số nguyên tố chia hết cho 7:", so_nguyen_to_7)
chinh_phuong = so_chinh_phuong(ngau_nhien)
if chinh_phuong:
    print("Các số chính phương trong dãy:", chinh_phuong)
else:
    print("Không có số chính phương trong dãy.")
