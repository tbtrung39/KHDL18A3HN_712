import datetime
ngay_1 = input("Nhập ngày thứ nhất (dd-mm-yyyy): ")
ngay_2 = input("Nhập ngày thứ hai (dd-mm-yyyy): ")
try:
    ngay_obj_1 = datetime.datetime.strptime(ngay_1, "%d-%m-%Y")
    ngay_obj_2 = datetime.datetime.strptime(ngay_2, "%d-%m-%Y")
    khoang_cach = abs(ngay_obj_2 - ngay_obj_1)
    ngay = khoang_cach.days
    nam = ngay // 365
    ngay_con_lai = ngay % 365
    thang = ngay_con_lai // 30
    ngay_le = ngay_con_lai % 30
    print(f"Khoảng cách: {nam} năm, {thang} tháng, {ngay_le} ngày")
except ValueError:
    print("Định dạng ngày không hợp lệ")