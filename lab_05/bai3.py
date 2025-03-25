chu_so = int(input("Nhập số tự nhiên: "))
if chu_so == 0:
    print("Chuỗi nhị phân:", 0)
else:
    c_nhi_phan = "" 
    while chu_so > 0:
        phan_du = chu_so % 2  
        c_nhi_phan = str(phan_du) + c_nhi_phan 
        chu_so = chu_so // 2  
    print("Chuỗi nhị phân:", c_nhi_phan)