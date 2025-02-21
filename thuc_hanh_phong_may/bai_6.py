t = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))
u = 220  
i = 2.7  
tien = 7000  
p = u * i 
a = (p * t) / (1000 * 3600) 
tienphaitra = a * tien  
print(f"Tiền điện phải trả: {round(tienphaitra, 2)} đồng")
