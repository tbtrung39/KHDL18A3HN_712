import qlyhanghoa

n = int(input("Nhap so luong mat hang: "))
ds = qlyhanghoa.nhap_danh_sach_hang(n)

print("\nDANH SACH TRUOC KHI SAP XEP:")
qlyhanghoa.hien_thi_danh_sach(ds)

ds_sapxep = qlyhanghoa.sap_xep_theo_thue(ds)
print("\nDANH SACH SAU KHI SAP XEP THEO THUE GIAM DAN:")
qlyhanghoa.hien_thi_danh_sach(ds_sapxep) 