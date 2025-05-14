import ds
n = int(input("Nhập số phần tử của dãy:"))
day = ds.tao_day(n)
print("Dãy số được sinh:",day)
print("Các số chia hết cho 7 là:",ds.so_chia_het_cho_7(day))
print("Tổng các số lẻ trong dãy:",ds.tong_so_le(day))

chinh_phuong = ds.cac_so_chinh_phuong(day)
if chinh_phuong:
    print("Các số chình phương trong dãy:",chinh_phuong)
else:
    print("Không có số chính phương trong dãy.")