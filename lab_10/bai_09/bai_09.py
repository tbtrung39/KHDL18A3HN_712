import quan_ly_hang_hoa

n = int(input("Nhập số lượng mặt hàng: "))
ds = quan_ly_hang_hoa.nhap_danh_sach_hang(n)

print("\nDANH SÁCH TRƯỚC KHI SẮP XẾP:")
quan_ly_hang_hoa.hien_thi_danh_sach(ds)

ds_sapxep = quan_ly_hang_hoa.sap_xep_theo_thue(ds)

print("\nDANH SÁCH SAU KHI SẮP XẾP THEO THUẾ GIẢM DẦN:")
quan_ly_hang_hoa.hien_thi_danh_sach(ds_sapxep)