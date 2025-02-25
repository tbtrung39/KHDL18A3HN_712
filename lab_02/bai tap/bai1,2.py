month = int(input("Nhập vào tháng (1-12): "))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("Tháng", month, "có 31 ngày.")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("Tháng", month, "có 30 ngày.")
elif month == 2:
    print("Tháng 2 có 28 hoặc 29 ngày (nếu là năm nhuận).")
else:
    print("Tháng không hợp lệ.")
