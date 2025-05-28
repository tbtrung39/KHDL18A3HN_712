from datetime import datetime
try:
    chuoi = input("Nhập ngày (định dạng dd-mm-yyyy): ")
    ngay = datetime.strptime(chuoi, "%d-%m-%Y")
    tuan_thu = ngay.isocalendar()[1]
    print(f"Ngày {ngay.strftime('%d-%m-%Y')} thuộc tuần thứ {tuan_thu} trong năm.")
except ValueError:
    print("Lỗi: Ngày không hợp lệ hoặc sai định dạng.")
