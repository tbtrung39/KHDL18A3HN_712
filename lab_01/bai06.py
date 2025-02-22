U = 220 # Hiệu điện thế (V)
I = 2.7 # Cường độ dòng điện (A)
gia_dien = 7000 # Giá điện (đ/KWh)
so_giay = int(input("Nhập thời gian sử dụng bóng đèn (giây): "))
P = U*I # Công suất P(W)

# Tính thời gian sử dụng (giờ)
t = so_giay/3600

# Tính lượng điện tiêu thụ (KWh)
A = (P*t)/1000 

# Tính số tiền điện phải trả
tien_phai_tra = A*gia_dien
tien_phai_tra = round(tien_phai_tra, 2)

print(f"Tiền điện phải trả: {tien_phai_tra} đồng")