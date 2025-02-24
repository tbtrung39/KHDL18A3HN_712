ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

la_nam_nhuan = (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)
if thang == 2:
    if la_nam_nhuan:
        so_ngay_trong_thang = 29
    else:
        so_ngay_trong_thang = 28
elif thang == 4:
    so_ngay_trong_thang = 30
elif thang == 6:
    so_ngay_trong_thang = 30
elif thang == 9:
    so_ngay_trong_thang = 30
elif thang == 11:
    so_ngay_trong_thang = 30
else:
    so_ngay_trong_thang = 31

if 1 <= thang <= 12 and 1 <= ngay <= so_ngay_trong_thang:
    if ngay < so_ngay_trong_thang:
        ngay += 1
    else:
        ngay = 1
        if thang < 12:
            thang += 1
        else:
            thang = 1
            nam += 1

    print(f"Ngày tiếp theo là: {ngay}/{thang}/{nam}")
else:
    print("Ngày nhập vào không hợp lệ.")