so = int(input("Nhập một số nguyên: "))  
nhi_phan = ""  

if so == 0:
    nhi_phan = "0"  
else:
    while so > 0:
        nhi_phan = str(so % 2) + nhi_phan  
        so = so // 2  

print(f"Số nhị phân tương ứng: {nhi_phan}")  
