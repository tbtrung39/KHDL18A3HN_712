from datetime import datetime, timedelta
try:
    ngay = int(input("Nhập ngày: "))
    thang = int(input("Nhập tháng: "))
    nam = int(input("Nhập năm: "))
    d = datetime(nam, thang, ngay)
    tuan = d.isocalendar().week
    print(f"Ngày {d.strftime('%d-%m-%Y')} thuộc tuần thứ {tuan} trong năm.")
except ValueError as ve:
    print("Lỗi định dạng ngày:", ve)
