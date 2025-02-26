ngay = int(input("Nhập vào ngày (1-31): "))
thang = int(input("Nhập vào tháng (1-12): "))
nam = int(input("Nhập vào năm: "))
so_ngay_trong_thang = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if 1 <= thang <= 12:
    if ngay < so_ngay_trong_thang[thang - 1]:
        ngay += 1
    else:
        ngay = 1  
        thang += 1  
        if thang > 12:
            thang = 1  
            nam += 1  
    print(f"Ngày tiếp theo: {ngay}/{thang}")
else:
    print("Tháng không hợp lệ")
