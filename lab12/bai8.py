import datetime

ngay = input("nhap ngay (dd-mm-yyyy): ")
try:
    ngay_obj = datetime.datetime.strptime(ngay, "%d-%m-%Y")
    ngay_truoc = ngay_obj - datetime.timedelta(days=1)
    print("ngay truoc do:", ngay_truoc.strftime("%d-%m-%Y"))
except ValueError:
    print("dinh dang khong hop le")