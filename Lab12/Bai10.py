from datetime import datetime
def khoang_cach_giua_hai_ngay(ngay1,ngay2):
    khoang_cach=abs(ngay2-ngay1)
    return khoang_cach.days
ngay_1=input("Nhap ngay 1 (dd-mm-yyyy):")
ngay_2=input("Nhap ngay 2 (dd-mm-yyyy):")
try:
    ngay1=datetime.strptime(ngay_1, "%d-%m-%Y")
    ngay2=datetime.strptime(ngay_2, "%d-%m-%Y")
    days=khoang_cach_giua_hai_ngay(ngay1,ngay2)
    print("Hai ngay cach nhau",days,"ngay.")
except ValueError:
    print("Khong hop le!")