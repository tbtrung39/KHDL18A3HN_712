#Bai9
str = input("Nhập chuỗi ký tự: ")  
ky_tu_xuat_hien_nhieu_nhat = ' '
chuoi_kt_con_cuc_dai = 0  
for char in str:  
    so_lan_xuat_hien = 0  
    for i in str:  
        if i == char:  
            so_lan_xuat_hien += 1  
    if so_lan_xuat_hien > chuoi_kt_con_cuc_dai:  
        chuoi_kt_con_cuc_dai = so_lan_xuat_hien  
        ky_tu_xuat_hien_nhieu_nhat = char  
ket_qua = ky_tu_xuat_hien_nhieu_nhat * chuoi_kt_con_cuc_dai  
print("Chuỗi ký tự con có độ dài cực đại:", ket_qua)