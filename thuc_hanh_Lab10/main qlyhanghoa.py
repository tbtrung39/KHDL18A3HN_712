import qlyhanghoa
danh_sach = qlyhanghoa.nhap_danh_sach_mat_hang()
print("\n--- Danh sách mặt hàng trước khi sắp xếp ---")
qlyhanghoa.in_danh_sach(danh_sach)
danh_sach_sap_xep = qlyhanghoa.sap_xep_theo_thue_giam_dan(danh_sach)
print("\n--- Danh sách mặt hàng sau khi sắp xếp theo thuế giảm dần ---")
qlyhanghoa.in_danh_sach(danh_sach_sap_xep)
