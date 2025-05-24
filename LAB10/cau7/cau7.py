from sinh_so import *

day=sinh_day_so()
print("Dãy số:",day)
print("Số nguyên tố chia hết cho 7:",so_nguyen_to_chia_het_7(day))
print("Tổng số lẻ:",tong_so_le(day))

scp=so_chinh_phuong(day)
if scp: print("Số chính phương trong dãy:",scp)
else: print("Không có số chính phương trong dãy")
