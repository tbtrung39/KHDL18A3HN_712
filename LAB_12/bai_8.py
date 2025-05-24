from datetime import datetime, timedelta

def bai8():
    try:
        date_str = input("Nhập ngày (định dạng dd-mm-yyyy): ")
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
        previous_day = date_obj - timedelta(days=1)
        print("Ngày trước đó là:", previous_day.strftime("%d-%m-%Y"))
    except ValueError:
        print("Lỗi: Định dạng ngày không hợp lệ. Hãy nhập theo dd-mm-yyyy.")
