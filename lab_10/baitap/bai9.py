from pkg import qlyhanghoa

n = int(input("Nhập số lượng mặt hàng: "))
ds = qlyhanghoa.nhap_danh_sach_hang(n)

print("\nDANH SÁCH TRƯỚC KHI SẮP XẾP:")
qlyhanghoa.hien_thi_danh_sach(ds)

ds_sapxep = qlyhanghoa.sap_xep_theo_thue(ds)

print("\nDANH SÁCH SAU KHI SẮP XẾP THEO THUẾ GIẢM DẦN:")
qlyhanghoa.hien_thi_danh_sach(ds_sapxep)