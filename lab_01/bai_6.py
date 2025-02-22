t = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))
P = 220 * 2.7  
dien_nang_tieu_thu = (P * t) / (1000 * 3600)  
tien_dien = dien_nang_tieu_thu * 7000
print("Tiền điện phải trả:", tien_dien, "đồng")