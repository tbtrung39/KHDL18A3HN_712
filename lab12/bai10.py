from datetime import datetime
from dateutil.relativedelta import relativedelta
def main():
    try:
        ngay_1_str = input("Nhap ngay thu nhat: ")
        ngay_2_str = input("Nhap ngay thu hai: ")
        ngay_1 = datetime.strptime(ngay_1_str, "%d-%m-%Y")
        ngay_2 = datetime.strptime(ngay_2_str, "%d-%m-%Y")
        if ngay_1 > ngay_2:
            ngay_1, ngay_2 = ngay_2, ngay_1
        khoang_cach = relativedelta(ngay_2, ngay_1)
        print(f"Hai ngay cach nhau: {khoang_cach.years} nam, {khoang_cach.months} thang, {khoang_cach.days} ngay.")
    except ValueError:
        print("Loi: Vui long nhap dung dinh dang ngay (dd-mm-yyyy).")
if __name__ == "__main__":
    main()
