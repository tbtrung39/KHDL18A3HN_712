import datetime
ngay = input("Nhập ngày (dd-mm-yyyy): ")
try:
    ngay_obj = datetime.datetime.strptime(ngay, "%d-%m-%Y")
    tuan = ngay_obj.isocalendar()[1]
    print("Ngày thuộc tuần thứ", tuan, "trong năm")
except ValueError:
    print("Định dạng ngày không hợp lệ")