#cau2:
s = int(input("Nhập số giây:"))
m = int(input("Nhập số phút:"))
h = int(input("Nhập số giờ:"))
d = int(input("Nhập số ngày:"))
tong_giay = d * 86400 + h * 3600 + m * 60 + s
ngay = tong_giay // 86400
tong_giay %= 86400
gio = tong_giay // 3600
tong_giay %= 3600
phut = tong_giay // 60
giay = tong_giay % 60
print(f"{ngay} ngày, {gio} giờ, {phut} phút, {giay} giây")