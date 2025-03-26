print('cách 1\n')
chuoi_nhi_phan = input("Nhập chuỗi số nhị phân: ")
so_thap_phan = int(chuoi_nhi_phan, 2)
print("Giá trị thập phân tương ứng là:", so_thap_phan)
print('cách2\n')
chuoi_nhi_phan = input("Nhập chuỗi số nhị phân: ")
so_thap_phan = 0
luy_thua = 1 
i = len(chuoi_nhi_phan) - 1
while i >= 0:
    if chuoi_nhi_phan[i] == '1':
        so_thap_phan += luy_thua 
    luy_thua *= 2 
    i -= 1 
print("Giá trị thập phân tương ứng là:", so_thap_phan)

