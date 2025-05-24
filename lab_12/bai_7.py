import datetime

def main():
    try:
        ngày = int(input("Nhập ngày: "))
        tháng = int(input("Nhập tháng: "))
        năm = int(input("Nhập năm: "))

        ngày_đã_nhập = datetime.date(năm, tháng, ngày)
        ngày_kế_tiếp = ngày_đã_nhập + datetime.timedelta(days=1)

        print("Ngày kế tiếp là:", ngày_kế_tiếp.strftime("%d/%m/%Y"))

    except ValueError:
        print("Lỗi: Ngày tháng năm không hợp lệ.")

if __name__ == "__main__":
    main()
