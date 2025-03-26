#giống bài 5
chuoi = input("Nhập chuỗi: ")
so = ""
for ky_tu in chuoi:
    if ky_tu.isdigit():
        so += ky_tu

print("Chuỗi số sau khi lọc:", so)
if so:
    so_nguyen = int(so)
    tong_uoc = 0

    for i in range(1, so_nguyen):
        if so_nguyen % i == 0:
            tong_uoc += i

    if tong_uoc == so_nguyen:
        print(so_nguyen, "là số hoàn hảo.")
    else:
        print(so_nguyen, "không phải là số hoàn hảo.")
else:
    print("Không có số hợp lệ.")