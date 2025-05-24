import dayso
ds = dayso.sinh_day_so()
print("Day so:", ds)
ds_so_chia_het_7 = dayso.liet_ke_chia_het_cho_7(ds)
print("Cac so chia het cho 7:", ds_so_chia_het_7)
tong = dayso.tong_day(ds)
print("Tong cac so:", tong)
if dayso.co_chinh_phuong(ds):
    print("Day so co so chinh phuong.")
else:
    print("Day so khong co so chinh phuong.")