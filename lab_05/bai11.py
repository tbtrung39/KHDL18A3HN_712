# cau 11
chuoi_nhi_phan = input("Nhập chuỗi số nhị phân: ")
so_thap_phan = 0
do_dai = len(chuoi_nhi_phan)
for i in range(do_dai):
    ky_tu = chuoi_nhi_phan[i]
    if ky_tu == '1': 
        so_thap_phan += 2 ** (do_dai - 1 - i)
print("Giá trị thập phânn là:", so_thap_phan)
