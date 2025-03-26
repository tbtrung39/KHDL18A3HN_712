n = int(input("Nhập số nguyên n: "))
chuoi_nhi_phan = ""
while n > 0:
    chuoi_nhi_phan = str(n % 2) + chuoi_nhi_phan
    n //= 2
print("Chuỗi nhị phân:", chuoi_nhi_phan)
