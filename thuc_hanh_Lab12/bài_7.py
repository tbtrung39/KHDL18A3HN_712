from datetime import datetime, timedelta
try:
    chuoi = input("Nhập ngày (định dạng dd-mm-yyyy): ")
    ngay = datetime.strptime(chuoi, "%d-%m-%Y")
    ngay_ketiep = ngay + timedelta(days=1)
    print("Ngày kế tiếp là:", ngay_ketiep.strftime("%d-%m-%Y"))
except ValueError:
    print("Lỗi: Ngày không hợp lệ hoặc sai định dạng.")
