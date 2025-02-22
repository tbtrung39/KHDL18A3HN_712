s = int(input("nhập số giây:"))
m = int(input("nhâp số phút:"))
h = int(input("nhập số giờ:"))
d = int(input("nhập số ngày:"))
tong_so_giay = s + (m*60) + (h*3600) + (d*86400)
ngay = tong_so_giay//86400
so_giay_con_lai = tong_so_giay%86400
gio = so_giay_con_lai//3600
so_giay_con_lai %= 3600
phut = so_giay_con_lai // 60
giay =so_giay_con_lai % 60
print(f"tổng cộng: {ngay} ngày, {gio} giờ, {phut} phút, {giay} giây")