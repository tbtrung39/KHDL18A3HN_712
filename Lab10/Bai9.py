import qlyhanghoa
ds = qlyhanghoa.nhap_du_lieu()
print("Danh sach truoc khi sap xep:")
qlyhanghoa.thong_tin(ds)
ds_sap_xep = qlyhanghoa.sap_xep_theo_thue(ds)
print("Danh sach sau khi sap xep theo thue:")
qlyhanghoa.hien_thi(ds_sap_xep)