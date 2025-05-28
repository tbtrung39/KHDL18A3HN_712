from datetime import datetime, timedelta
try:
    chuoi = input("Nhập ngày (định dạng dd-mm-yyyy): ")
    ngay = datetime.strptime(chuoi, "%d-%m-%Y")
    ngay_truoc = ngay - timedelta(days=1)
    print("Ngày trước đó là:", ngay_truoc.strftime("%d-%m-%Y"))
except ValueError:
    print("Lỗi: Ngày không hợp lệ hoặc sai định dạng.")
