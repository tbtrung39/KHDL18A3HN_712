thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
if thang == 1:
    print("Tháng có 31 ngày")
elif thang == 2:
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        print("Tháng 2 có 29 ngày")
    else:
        print("Tháng 2 có 28 ngày")
elif thang == 3:
    print("Tháng 3 có 31 ngày")
elif thang == 4:
    print("Tháng 4 có 30 ngày")
elif thang == 5:
    print("Tháng 5 có 31 ngày")
elif thang == 6:
    print("Tháng 6 có 30 ngày")
elif thang == 7:
    print("Tháng 7 có 31 ngày")
elif thang == 8:
    print("Tháng 8 có 30 ngày")
elif thang == 9:
    print("Tháng 9 có 31 ngày")
elif thang == 10:
    print("Tháng 10 có 30 ngày")
elif thang == 11:
    print("Tháng 11 có 31 ngày")
elif thang == 12:
    print("Tháng 12 có 30 ngày")