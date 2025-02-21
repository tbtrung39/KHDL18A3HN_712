d = int(input("Nhập số ngày: "))
h = int(input("Nhập số giờ: "))
m = int(input("Nhập số phút: "))
s = int(input("Nhập số giây: "))
tong_giay = d * 86400 + h * 3600 + m * 60 + s
tong_ngay = tong_giay / 86400
tong_gio = tong_giay / 3600
tong_phut = tong_giay / 60
print("Tổng số giây:", tong_giay)
print("Tổng số phút:", tong_phut)
print("Tổng số giờ:", tong_gio)
print("Tổng số ngày:", tong_ngay)