import datetime

ngay = input("Nhập ngày (dd-mm-yyyy): ")
try:
    ngay_obj = datetime.datetime.strptime(ngay, "%d-%m-%Y")
    ngay_ke = ngay_obj + datetime.timedelta(days=1)
    print("Ngày kế tiếp:", ngay_ke.strftime("%d-%m-%Y"))
except ValueError:
    print("Định dạng ngày không hợp lệ")