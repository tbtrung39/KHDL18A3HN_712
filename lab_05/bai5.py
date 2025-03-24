# cau 5
c_ky_tu = input("Nhập chuỗi ký tự: ")
chuoi_so = ""
for ky_tu in c_ky_tu:
    if ky_tu.isdigit():  
        chuoi_so += ky_tu  
if chuoi_so == "":
    so_nguyen = 0
else:
    so_nguyen = int(chuoi_so)  
def la_so_hoan_hao(n):
    if n <= 0:
        return False
    tong_uoc = sum(i for i in range(1, n) if n % i == 0)
    return tong_uoc == n
print("Chuỗi số sau khi lọc:", chuoi_so)
if la_so_hoan_hao(so_nguyen):
    print(so_nguyen, "là số hoàn hảo.")
else:
    print(so_nguyen, "không phải là số hoàn hảo.")
