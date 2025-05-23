from datetime import datetime, timedelta

try:
    ngay = int(input("Nhập ngày: "))
    thang = int(input("Nhập tháng: "))
    nam = int(input("Nhập năm: "))
    d = datetime(nam, thang, ngay)
    ngay_ke = d + timedelta(days=1)
    print("Ngày kế tiếp:", ngay_ke.strftime("%d-%m-%Y"))
except ValueError as ve:
    print("Lỗi định dạng ngày:", ve)