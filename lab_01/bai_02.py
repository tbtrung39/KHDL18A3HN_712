s = float(input("Nhập số giây: "))
m = float(input("Nhập số phút: "))
h = float(input("Nhập số giờ: "))
d = float(input("Nhập số ngày: "))
x = s + m*60 +h*3600 + d*86400
print("Tổng số giây: ", x)