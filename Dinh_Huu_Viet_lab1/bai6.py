#cau6:
t = int(input("Nhập số giây sử dụng bóng đèn: "))
h = t / 3600
gia_dien = 7000
A = (220 * 2.7) / 1000
tien_dien_phai_tra = A * h * gia_dien
print("Giá tiền điện phải trả là:", tien_dien_phai_tra, "đồng")