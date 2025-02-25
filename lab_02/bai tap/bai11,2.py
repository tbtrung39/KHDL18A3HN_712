ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))

if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
    so_ngay = 31
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    so_ngay = 30
elif thang == 2:
    so_ngay = 28
else:
    print("Tháng không hợp lệ.")
    so_ngay = -1

if 1 <= ngay <= so_ngay:
    if ngay < so_ngay:
        ngay += 1
    else:
        ngay = 1
        thang += 1
        if thang > 12:
            thang = 1
    print("Ngày tiếp theo là:", ngay, "/", thang)
else:
    print("Ngày không hợp lệ.")
