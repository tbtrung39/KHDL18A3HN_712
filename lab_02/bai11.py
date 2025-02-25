ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))

if 1 <= thang <= 12 and 1 <= ngay <= ngay_trong_thang[thang - 1]:
    if ngay == ngay_trong_thang[thang - 1]:
        ngay = 1
        thang += 1
        if thang > 12:
            thang = 1
    else:
        ngay += 1
    print(f"Ngày tiếp theo: {ngay}/{thang}")
else:
    print("Ngày hoặc tháng không hợp lệ.")