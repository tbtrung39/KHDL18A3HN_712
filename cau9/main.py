import qlyhanghoa
ds = qlyhanghoa.nhap_danh_sach_mat_hang()
print("\nDANH SACH MAT HANG BAN DA NHAP:")
qlyhanghoa.hien_thi_danh_sach(ds)
print("\nDANH SACH SAU KHI SAP XEP GIAM DAN THEO THUE:")
ds_sap_xep = qlyhanghoa.sap_xep_theo_thue(ds)
qlyhanghoa.hien_thi_danh_sach(ds_sap_xep)
