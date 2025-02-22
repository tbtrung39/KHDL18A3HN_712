thoi_gian_sd=int(input("nhập thời gian theo đon vị giây: "))
hdt=220 
cddd=2.7 
gia_tien=7000 
cong_suat=hdt*cddd 
dien_nang_tieu_thu=(cong_suat*thoi_gian_sd)/3600000 #đơn vị kWh 
tien_dien_phai_tra=dien_nang_tieu_thu*gia_tien
print("tiền điện phải trả",tien_dien_phai_tra,"nghìn")