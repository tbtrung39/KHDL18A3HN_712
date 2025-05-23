import datetime

def tim_ngay():
    try:
        ngay = int(input("Nhập ngày: "))
        thang = int(input("Nhập tháng: "))
        nam = int(input("Nhập năm: "))

        d = datetime.date(ngay, thang, nam)

        week_number = d.isocalendar().week

        print(f"📅 Ngày {d.strftime('%d-%m-%Y')} thuộc tuần thứ {week_number} trong năm.")

    except ValueError :
        print("Lỗi: Vui lòng nhập ngày hợp lệ!")

tim_ngay()
