t = float(input("Nhap thoi gian su dung bong den(giay): "))
U = 220 
I = 2.7 
gia_dien = 7000 
dien_nang = (U*I*t) / (3600*1000)
tien_dien = dien_nang*gia_dien
print(f"So tien dien phai tra: {tien_dien:.2f} dong")
