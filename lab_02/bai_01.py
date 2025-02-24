nam = int(input("Nhap nam: "))
thang = int(input("Nhap thanh ban muon kiem tra: "))
#Nam nhuan:
if (nam % 4 == 0 and nam %100 != 0) or (nam % 400 == 0):
    if thang % 2 == 0 and thang != 2:
        print(f"{thang} co 30 ngay")
    elif thang % 2 != 0:
        print(f"{thang} co 31 ngay")
    elif thang == 2:
        print(f"{thang} co 29 ngay")
#Nam khong nhuan:
else:
    if thang % 2 == 0 and thang != 2:
        print(f"{thang} co 30 ngay")
    elif thang % 2 != 0:
        print(f"{thang} co 31 ngay")
    elif thang == 2:
        print(f"{thang} co 28 ngay")