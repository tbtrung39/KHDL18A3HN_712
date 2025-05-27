import datetime

ngay = input("Nhap ngay (dd-mm-yyyy): ")
try:
    ngay_obj = datetime.datetime.strptime(ngay, "%d-%m-%Y")
    ngay_ke = ngay_obj + datetime.timedelta(days=1)
    print("Ngay ke tiep:", ngay_ke.strftime("%d-%m-%Y"))
except ValueError:
    print("Dinh dang khong hop le!!!")