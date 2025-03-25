chuoi_nhi_phan = input("Nhập chuỗi nhị phân: ")
thap_phan = 0  
luy_thua = 0  

for i in range(len(chuoi_nhi_phan) - 1, -1, -1): 
    if chuoi_nhi_phan[i] == '1':  
        thap_phan += 2 ** luy_thua 
    luy_thua += 1 

print("Giá trị thập phân:", thap_phan)
