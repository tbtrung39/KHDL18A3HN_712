import dayso

n = int(input("Nhap so phan tu cua day:"))
day = dayso.sinh_day_so(n)
print("Day so duoc sinh:",day)
print("Cac so chia het cho 7 la:",dayso.so_nguyen_to_chia_het_cho_7(day))
print("Tong cac so le trong day:",dayso.tong_so_le(day))

chinh_phuong = dayso.la_so_chinh_phuong(day)
if chinh_phuong:
    print("Cac so chinh phuong trong day:",chinh_phuong)
else:
    print("Khong co so chinh phuong trong day.")