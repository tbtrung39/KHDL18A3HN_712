from qlyhanghoa import *

ds=nhap_danh_sach()

tinh_thanh_tien(ds)
tinh_thue(ds)

print("Trước sắp xếp:")
in_danh_sach(ds)

sap_xep_thue(ds)

print("Sau sắp xếp:")
in_danh_sach(ds)
