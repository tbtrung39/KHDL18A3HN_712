day = int(input("Nhập ngày (1-31): "))
month = int(input("Nhập tháng (1-12): "))
year = int(input("Nhập năm: "))
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    max_day = 31
elif month == 4 or month == 6 or month == 9 or month == 11:
    max_day = 30
elif month == 2:
    max_day = 28
else:
    max_day = 0
if month < 1 or month > 12 or day < 1 or day > max_day:
    print("Ngày hoặc tháng không hợp lệ.")
else:
    day += 1
    if day > max_day:
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    print(f"Ngày tiếp theo là: {day}/{month}/{year}")