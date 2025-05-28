from datetime import datetime
try:
    chuoi1 = input("Nhập ngày thứ nhất (dd-mm-yyyy): ")
    chuoi2 = input("Nhập ngày thứ hai (dd-mm-yyyy): ")
    ngay1 = datetime.strptime(chuoi1, "%d-%m-%Y")
    ngay2 = datetime.strptime(chuoi2, "%d-%m-%Y")
    khoang_cach = abs((ngay2 - ngay1).days)
    print(f"Hai ngày cách nhau {khoang_cach} ngày.")
    nam = khoang_cach // 365
    thang = (khoang_cach % 365) // 30
    ngay = (khoang_cach % 365) % 30
    print(f"Ước lượng: {nam} năm, {thang} tháng, {ngay} ngày.")
except ValueError:
    print("Lỗi: Một trong hai ngày không hợp lệ hoặc sai định dạng.")
