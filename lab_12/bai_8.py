import datetime

def main():
    try:
        ngày = int(input("Nhập ngày: "))
        tháng = int(input("Nhập tháng: "))
        năm = int(input("Nhập năm: "))

        ngày_đã_nhập = datetime.date(năm, tháng, ngày)
        ngày_trước = ngày_đã_nhập - datetime.timedelta(days=1)

        print("Ngày trước đó là:", ngày_trước.strftime("%d/%m/%Y"))

    except ValueError:
        print("Lỗi: Ngày tháng năm không hợp lệ.")

if __name__ == "__main__":
    main()
