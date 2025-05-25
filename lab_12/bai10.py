from datetime import datetime
try:
    ngay = input("Nhap ngay(dd-mm-yyyy):")
    d=datetime.strftime(ngay,"%d-%m-%y")
    thu=d.strftime("%A")
    thu_viet={
        "monday":"thu2",
        "tuesday":"thu3",
        "wednesday":"thu4",
        "thursday":"thu5",
        "friday":"thu6",
        "saturday":"thu7",
        "sunday":"chu nhat"
    }
    print("do la:",thu_viet[thu])
except ValueError:
    print("loi: ngay khong hop le")