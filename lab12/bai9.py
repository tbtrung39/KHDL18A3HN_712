import datetime

def main():
    try:
        ngay = int(input("Nhap ngay: "))
        thang = int(input("Nhap thang: "))
        nam = int(input("Nhao nam: "))
        ngay_duoc_nhap = datetime.date(nam, thang, ngay)
        so_tuan = ngay_duoc_nhap.isocalendar()[1]
        print(f"Ngay {ngay_duoc_nhap.strftime('%d/%m/%Y')} thuoc tuan thu {so_tuan} trong nam {nam}.")

    except ValueError:
        print("Ngay khong hop le. Vui long kiem tra lai.")
if __name__ == "__main__":
    main()