from datetime import datetime, timedelta
ngay_str=input("Nhap (dd-mm-yyyy):")
try:
    ngay=datetime.strptime(ngay_str,"%d-%m-%Y")
    ngay_truoc_do=ngay-timedelta(days=1)
    print("Ngay truoc do la:", ngay_truoc_do.strftime("%d-%m-%Y"))
except ValueError:
    print("Khong hop le!")