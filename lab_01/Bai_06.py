t = float(input('Nhập thời gian sử dụng bóng đèn: '))
u = 220  
i = 2.7 
gia_tien = 7000  
cong_suat = u * i 
nang_luong_tieu_thu_kwh = (cong_suat * t) / (1000 * 3600) 
tien_dien = nang_luong_tieu_thu_kwh * gia_tien
print(f'Tiền điện phải trả: {tien_dien:.2f} đ')