c_ky_tu = input("Nhập chuỗi ký tự: ")
chuoi_so = ""
for ky_tu in c_ky_tu:
    if ky_tu.isdigit():
        chuoi_so += ky_tu  
if chuoi_so == "":
    so_nguyen = 0
else:
    so_nguyen = int(chuoi_so)
tong_uoc = 0
for i in range(1, so_nguyen):
    if so_nguyen % i == 0:
        tong_uoc += i  
print("Chuỗi số sau khi lọc:", chuoi_so)
if tong_uoc == so_nguyen and so_nguyen > 0:
    print(so_nguyen, "là số hoàn hảo.")
else:
    print(so_nguyen, "không phải là số hoàn hảo.")
