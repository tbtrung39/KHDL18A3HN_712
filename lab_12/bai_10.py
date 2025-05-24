from datetime import datetime

def tính_khoảng_cách(ngày_1, ngày_2):
    if ngày_1 > ngày_2:
        ngày_1, ngày_2 = ngày_2, ngày_1

    năm = ngày_2.year - ngày_1.year
    tháng = ngày_2.month - ngày_1.month
    ngày = ngày_2.day - ngày_1.day

    if ngày < 0:
        tháng -= 1
        tháng_trước = (ngày_2.month - 1) if ngày_2.month > 1 else 12
        năm_của_tháng_trước = ngày_2.year if ngày_2.month > 1 else ngày_2.year - 1
        ngày_trong_tháng_trước = (datetime(năm_của_tháng_trước, tháng_trước + 1, 1) - datetime(năm_của_tháng_trước, tháng_trước, 1)).days
        ngày += ngày_trong_tháng_trước

    if tháng < 0:
        năm -= 1
        tháng += 12

    return năm, tháng, ngày

def main():
    try:
        chuỗi_ngày_1 = input("Nhập ngày thứ nhất: ").strip()
        chuỗi_ngày_2 = input("Nhập ngày thứ hai: ").strip()

        định_dạng = "%d-%m-%Y"
        ngày_1 = datetime.strptime(chuỗi_ngày_1, định_dạng)
        ngày_2 = datetime.strptime(chuỗi_ngày_2, định_dạng)

        năm, tháng, ngày = tính_khoảng_cách(ngày_1, ngày_2)

        print(f"Hai ngày cách nhau {năm} năm, {tháng} tháng, {ngày} ngày.")

    except ValueError:
        print("Lỗi: Ngày nhập không đúng định dạng hoặc không hợp lệ.")

if __name__ == "__main__":
    main()

