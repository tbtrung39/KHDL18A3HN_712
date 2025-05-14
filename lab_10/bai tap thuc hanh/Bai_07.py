from pkg import dayso
n=int(input("Nhập số phần tử của dãy:"))
day=dayso.tao_day(n)
print("Dãy số được sinh:",day)
print("Các số chia hết cho 7 là:",dayso.so_chia_het_cho_7(day))
print("Tổng các số lẻ trong dãy:",dayso.tong_so_le(day))

chinh_phuong=dayso.cac_so_chinh_phuong(day)
if chinh_phuong:
    print("Các số chình phương trong dãy:",chinh_phuong)
else:
    print("Không có số chính phương trong dãy.")