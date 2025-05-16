import qlyhanghoa

print("=== QUẢN LÝ HÀNG HÓA SIÊU THỊ ===")

danh_sach = qlyhanghoa.nhap_mat_hang()
qlyhanghoa.tinh_thanh_tien_va_thue(danh_sach)

print("\n--- DANH SÁCH TRƯỚC KHI SẮP XẾP ---")
qlyhanghoa.in_danh_sach(danh_sach)

danh_sach_sx = qlyhanghoa.sap_xep_giam_theo_thue(danh_sach)
print("\n--- DANH SÁCH SAU KHI SẮP XẾP GIẢM DẦN THEO THUẾ ---")
qlyhanghoa.in_danh_sach(danh_sach_sx)
