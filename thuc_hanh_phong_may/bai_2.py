tong_so_giay = int(input("Nhập tổng số giây: ")) 
d = tong_so_giay // (24 * 3600) 
du = tong_so_giay % (24 * 3600) 
h = du // 3600 
du = du % 3600 
m = du // 60 
s = du % 60 
print(f"{d} ngày, {h} giờ, {m} phút, {s} giây") 