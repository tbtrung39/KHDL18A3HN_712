import datetime

ngay = input("nhap ngay (dd-mm-yyyy): ")
try:
    ngay_obj = datetime.datetime.strptime(ngay, "%d-%m-%Y")
    tuan = ngay_obj.isocalendar()[1]
    print("ngay thuoc tuan thu", tuan, "trong nam")
except ValueError:
    print("dinh dang khong hop le")