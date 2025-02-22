t = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))
P = 220 * 2.7  # công suất tiêu thụ 
E_kWh = (P * t) / (1000 * 3600)  # Điện năng tiêu thụ
tien_dien = E_kWh * 7000
print("Tiền điện phải trả:", tien_dien, "đồng")
