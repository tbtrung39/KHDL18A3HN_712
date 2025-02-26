kw_tieu_thu = float(input("Nhập số KW điện tiêu thụ: "))

if 0 <= kw_tieu_thu <= 100:
    don_gia = 2000
elif 101 <= kw_tieu_thu <= 200:
    don_gia = 2500
elif 201 <= kw_tieu_thu <= 300:
    don_gia = 3000
elif kw_tieu_thu > 300:
    don_gia = 5000
else:
    don_gia = 0  

tien_dien = kw_tieu_thu * don_gia

if kw_tieu_thu < 0:
    print("Số KW không hợp lệ.")
else:
    print("Tiền điện phải trả là: ", tien_dien, "đồng")