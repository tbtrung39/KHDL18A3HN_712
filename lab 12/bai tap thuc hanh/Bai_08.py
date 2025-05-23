from datetime import datetime,timedelta
try:
    ngay=int(input("Nhập ngày:"))
    thang=int(input("Nhập tháng:"))
    nam=int(input("Nhập năm:"))
    d=datetime(nam,thang,ngay)
    ngay_truoc=d-timedelta(days=1)
    print("Ngày trước:",ngay_truoc.strftime("%d-%m-%Y"))
except ValueError as e:
    print(e)