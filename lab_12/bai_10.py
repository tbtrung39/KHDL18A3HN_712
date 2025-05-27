import datetime
ngay_1 = input("Nhap ngay thu nhat (dd-mm-yyyy): ")
ngay_2 = input("Nhap ngay thu hai (dd-mm-yyyy): ")
try:
    ngay_obj_1 = datetime.datetime.strptime(ngay_1, "%d-%m-%Y")
    ngay_obj_2 = datetime.datetime.strptime(ngay_2, "%d-%m-%Y")
    khoang_cach = abs(ngay_obj_2 - ngay_obj_1)
    ngay = khoang_cach.days
    nam = ngay // 365
    ngay_con_lai = ngay % 365
    thang = ngay_con_lai // 30
    ngay_le = ngay_con_lai % 30
    print(f"Khoang cach: {nam} nam, {thang} thang, {ngay_le} ngay")
except ValueError:
    print("Dinh dang ngay khong hop le!!!")