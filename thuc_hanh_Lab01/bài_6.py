t = float(input("thời gian sử dụng bóng đèn : "))
U = 220  
I = 2.7 
gia_dien = 7000  
# Tính công suất tiêu thụ 
P = U * I  
# Tính năng lượng tiêu thụ
W = P * t  
# Đổi sang kWh
E = W / 3600000  
# Tính tiền điện
tien_dien = E * gia_dien  
print(f"Tiền điện phải trả: {tien_dien:.2f} đồng")
