# main_bai7.py
import bai_7
n = int(input("Nhập số lượng phần tử: "))
ds = bai_7.sinh_day_so(n)
print("Dãy số:", ds)
print("Các số chia hết cho 7:", bai_7.liet_ke_chia_het_cho_7(ds))
print("Tổng các số lẻ:", bai_7.tong_so_le(ds))
so_cp = bai_7.kiem_tra_chinh_phuong(ds)
if so_cp:
    print("Các số chính phương:", so_cp)
else:
    print("Không có số chính phương.")
