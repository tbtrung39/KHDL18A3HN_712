from doicoso import doicoso1, doicoso2

n = doicoso1.nhap_so()
print("Số vừa nhập:", n)
print("Nhị phân:", doicoso1.sang_nhi_phan(n))
print("Bát phân:", doicoso1.sang_bat_phan(n))
print("Thập lục phân:", doicoso1.sang_thap_luc_phan(n))

s = input("Nhập chuỗi: ")
s = doicoso2.loc_ky_tu(s)
print("Chuỗi sau lọc:", s)
cs = doicoso2.co_so(s)
print("Cơ số:", cs)

for base, func in [(2, doicoso2.tu_co_so_2), (8, doicoso2.tu_co_so_8), (16, doicoso2.tu_co_so_16)]:
    result = func(s)
    print(f"Cơ số {base} sang 10:", result if isinstance(result, str) else int(result))
