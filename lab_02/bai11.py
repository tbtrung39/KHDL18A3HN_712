ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
so_ngay_trong_thang = 0

if thang == 1:
    so_ngay_trong_thang = 31
elif thang == 2:
    so_ngay_trong_thang = 28
elif thang == 3:
    so_ngay_trong_thang = 31
elif thang == 4:
    so_ngay_trong_thang = 30
elif thang == 5:
    so_ngay_trong_thang = 31
elif thang == 6:
    so_ngay_trong_thang = 30
elif thang == 7:
    so_ngay_trong_thang = 31
elif thang == 8:
    so_ngay_trong_thang = 31
elif thang == 9:
    so_ngay_trong_thang = 30
elif thang == 10:
    so_ngay_trong_thang = 31
elif thang == 11:
    so_ngay_trong_thang = 30
elif thang == 12:
    so_ngay_trong_thang = 31

if ngay < so_ngay_trong_thang:
    ngay = ngay + 1
else:
    ngay = 1
    if thang < 12:
        thang = thang + 1
    else:
        thang = 1
        nam = nam + 1
print("Ngày tiếp theo là: ", ngay, "/", thang, "/", nam)