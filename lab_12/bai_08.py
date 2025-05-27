import datetime

ngay = input("Nhap ngay (dd-mm-yyyy): ")
try:
    ngay_obj = datetime.datetime.strptime(ngay, "%d-%m-%Y")
    ngay_truoc = ngay_obj - datetime.timedelta(days=1)
    print("Ngay truoc do:", ngay_truoc.strftime("%d-%m-%Y"))
except ValueError:
    print("Dinh dang khong hop le!!!")