from datetime import datetime, timedelta

def tinh_khoang_cach(d1, d2):
    if d1 > d2:
        d1, d2 = d2, d1

    nam, thang, ngay = 0, 0, 0
    temp = d1

    while True:
        try:
            tmp = datetime(temp.year + 1, temp.month, temp.day)
            if tmp <= d2:
                nam += 1
                temp = tmp
            else:
                break
        except:
            temp = datetime(temp.year + 1, temp.month, temp.day - 1)
            nam += 1

    while True:
        try:
            if temp.month == 12:
                tmp = datetime(temp.year + 1, 1, temp.day)
            else:
                tmp = datetime(temp.year, temp.month + 1, temp.day)
            if tmp <= d2:
                thang += 1
                temp = tmp
            else:
                break
        except:
            temp = datetime(temp.year, temp.month + 1 if temp.month < 12 else 1, temp.day - 1)
            thang += 1


    while True:
        tmp = temp + timedelta(days=1)
        if tmp <= d2:
            ngay += 1
            temp = tmp
        else:
            break

    return nam, thang, ngay


try:
    d1_str = input("Nhập ngày thứ nhất (dd-mm-yyyy): ")
    d2_str = input("Nhập ngày thứ hai (dd-mm-yyyy): ")

    d1 = datetime.strptime(d1_str, "%d-%m-%Y")
    d2 = datetime.strptime(d2_str, "%d-%m-%Y")

    y, m, d = tinh_khoang_cach(d1, d2)
    print(f"Hai ngày cách nhau: {y} năm, {m} tháng, {d} ngày.")
except ValueError as ve:
    print("Lỗi định dạng ngày:", ve)
