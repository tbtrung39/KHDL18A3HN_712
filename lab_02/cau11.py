ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10:
    tong_ngay = 31
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    tong_ngay = 30
elif thang == 2:
    tong_ngay = 28
elif thang == 12:
    tong_ngay = 31
else:
    tong_ngay = 0

if 1 <= thang <= 12 and 1 <= ngay <= tong_ngay:
    if ngay < tong_ngay:
        ngay += 1
    else:
        ngay = 1
        thang = thang + 1 if thang < 12 else 1
    print(f"Ngày tiếp theo: {ngay}/{thang}")
else:
    print("Ngày không hợp lệ!")
