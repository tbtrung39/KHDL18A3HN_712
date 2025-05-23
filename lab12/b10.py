from datetime import datetime

try:
    ngay1s = input("Nhap ngay thu nhat (dd-mm-yyyy): ")
    ngay2s = input("Nhap ngay thu hai (dd-mm-yyyy): ")
    ngay1 = datetime.strptime(ngay1s, "%d-%m-%Y")
    ngay2 = datetime.strptime(ngay2s, "%d-%m-%Y")

    if ngay1 > ngay2:
        ngay1, ngay2 = ngay2, ngay1

    # Tính tổng số ngày chênh lệch
    delta_days = (ngay2 - ngay1).days

    # Tạm ước lượng: 1 năm = 365 ngày, 1 tháng = 30 ngày
    years = delta_days // 365
    months = (delta_days % 365) // 30
    days = (delta_days % 365) % 30

    print(f"Hai ngay cach nhau xap xi {years} nam, {months} thang, {days} ngay")
except ValueError:
    print("Loi: Dinh dang ngay khong dung (dd-mm-yyyy)")

