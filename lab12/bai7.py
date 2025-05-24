import datetime

def main():
    try:
        ngay = int(input("Nhap ngay: "))
        thang = int(input("Nhap thang: "))
        nam = int(input("Nhao nam: "))
        ngay_hien_tai = datetime.date(nam, thang, ngay)
        ngay_ke_tiep = ngay_hien_tai + datetime.timedelta(days = 1)
        print(f"Ngay ke tiep la: {ngay_ke_tiep.strftime('%d/%m/%Y')}")

    except ValueError:
        print("Ngay khong hop le. Vui long kiem tra lai.")
if __name__ == "__main__":
    main()