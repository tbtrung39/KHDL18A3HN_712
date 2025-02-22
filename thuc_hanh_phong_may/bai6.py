thoi_gian=float(input("nhap thoi gian su dung bong 
# thong so cua bong den
hieu_dien_the=220
cuong_do_dong_dien=2.7
# tinh cong suat tieu thu
cong_suat=hieu_dien_the*cuong_do_dong_dien
nang_luong_tieu_thu=(cong_suat*thoi_gian)/(1000*360
# tinh tien
tien_dien=nang_luong_tieu_thu*7000
print(f"tien dien phai tra la {tien_dien:.2f} VND")
