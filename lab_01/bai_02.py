d = int(input("Nhập số ngày: "))
h = int(input("Nhập số giờ: "))
m = int(input("Nhập số phút: "))
s = int(input("Nhập số giây: "))

tong_giay = d*86400 + h*3600 + m*60 + s

print(f"Tổng số giây: {tong_giay} giây")