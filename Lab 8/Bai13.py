#Bai13
def ktra_nam_nhuan(y):
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        return True
    else:
        return False
def ngay_toi_da_thang(m, y):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30
    elif m == 2:
        if ktra_nam_nhuan(y):
            return 29
        else:
            return 28
    else:
        return -1
y = int(input("Nhap nam: "))
m = int(input("Nhap thang: "))
if ktra_nam_nhuan(y):
    print("Nam", y, "la nam nhuan.")
else:
    print("Nam", y, "khong phai la nam nhuan.")
so_ngay = ngay_toi_da_thang(m, y)
if so_ngay == -1:
    print("Thang khong hop le!")
else:
    print("Thang", m, "nam", y, "co", so_ngay, "ngay.")