from datetime import datetime, timedelta
ngay_str=input("Nhap (dd-mm-yyyy):")
try:
    ngay=datetime.strptime(ngay_str,"%d-%m-%Y")
    ngay_ke_tiep=ngay+timedelta(days=1)
    print("Ngay ke tiep la:", ngay_ke_tiep.strftime("%d-%m-%Y"))
except ValueError:
    print("Khong hop le!")