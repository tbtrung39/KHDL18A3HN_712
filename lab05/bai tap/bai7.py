chuoi = input("Nhập chuỗi ký tự: ")
chuoi_so = ""

for ky_tu in chuoi:
    if ky_tu.isdigit():
        chuoi_so += ky_tu  

if chuoi_so:
    so_nguyen = int(chuoi_so)  
    print("Chuỗi số sau khi lọc:", so_nguyen)

    tong_uoc = 0
    for i in range(1, so_nguyen):  
        if so_nguyen % i == 0:
            tong_uoc += i  

    if tong_uoc == so_nguyen:
        print(so_nguyen, "là số hoàn hảo.")
    else:
        print(so_nguyen, "không phải là số hoàn hảo.")
else:
    print("Chuỗi không chứa số nào.")
