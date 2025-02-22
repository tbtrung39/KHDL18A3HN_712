# Bài 6: 
t=float(input("Nhập thời gian sử dụng bóng đèn:")) 
u=220 
i=2.7 
gia_tien_dien=7000 
p=u*i 
w=p*t 
e=w/3600000 
tien_dien_phai_tra=e*gia_tien_dien 
print(f"Tiền điện phải trả là:{tien_dien_phai_tra:0.2f} đồng")