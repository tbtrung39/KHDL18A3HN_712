from pkg import xulydayso

ds = xulydayso.sinh_day_so()
print("Dãy số sinh ra:", ds)

print("Các số nguyên tố chia hết cho 7:", xulydayso.so_nguyen_to_chia_het_7(ds))
print("Tổng các số lẻ:", xulydayso.tong_so_le(ds))

cp = xulydayso.kiem_tra_chinh_phuong(ds)
if cp:
    print("Các số chính phương:", cp)
else:
    print("Không có số chính phương trong dãy.")
