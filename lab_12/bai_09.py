import datetime

ngay = input("Nhap ngay (dd-mm-yyyy): ")
try:
    ngay_obj = datetime.datetime.strptime(ngay, "%d-%m-%Y")
    tuan = ngay_obj.isocalendar()[1]
    print("Ngay thuoc tuan thu", tuan, "trong nam")
except ValueError:
    print("Dinh dang khong hop le!!!")