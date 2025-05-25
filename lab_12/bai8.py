from datetime import datetime, timedelta
try:
    ngay=input("nhap ngay(dd-mm-yyyy):")
    d =datetime.strftime(ngay,"%d-%m-%y")
    ngay_ke_tiep = d - timedelta(days=1)
    print("ngay ke tiep la:", ngay_ke_tiep.strftime("%d-%m-%y"))
except ValueError:
    print("loi: ngay khong hop le")