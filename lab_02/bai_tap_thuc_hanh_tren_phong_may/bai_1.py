thang = input("Nhập tháng (1->12): ")

if thang.isdigit():
    thang = int(thang)
    if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
        print("Tháng", thang, "có 31 ngày.")
    elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
        print("Tháng", thang, "có 30 ngày.")
    elif thang == 2:
        print("Tháng 2 có 28 hoặc 29 ngày.")
    else:
        print("Tháng không hợp lệ.")
else:
    print("Vui lòng nhập một số nguyên từ 1 đến 12.")