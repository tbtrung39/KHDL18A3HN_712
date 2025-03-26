Str = input("Nhap chuoi: ")
chuoi = ""
for i in Str:
    if i.isdigit():
        chuoi += i
if chuoi:
    so = int(chuoi)
    tong = 0
    for j in range(1, so):
        if so % j == 0:
            tong += j
    if tong == so:
        print("Chuoi con lai la so hoan hao")
    else:
        print("Chuoi con lai khong phai so hoan hao")
                
        