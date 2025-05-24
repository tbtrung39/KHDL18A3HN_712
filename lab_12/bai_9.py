import datetime

def main():
    try:
        ngày = int(input("Nhập ngày: "))
        tháng = int(input("Nhập tháng: "))
        năm = int(input("Nhập năm: "))

        ngày_đã_nhập = datetime.date(năm, tháng, ngày)
        tuần_thứ = ngày_đã_nhập.isocalendar()[1]  

        print(f"Ngày {ngày_đã_nhập.strftime('%d/%m/%Y')} thuộc tuần thứ {tuần_thứ} trong năm {năm}.")

    except ValueError:
        print("Lỗi: Ngày tháng năm không hợp lệ.")

if __name__ == "__main__":
    main()
