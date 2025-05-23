import datetime

try:
    day = int(input("Nhap ngay: "))
    month = int(input("Nhap thang: "))
    year = int(input("Nhap nam: "))
    
    hn = datetime.date(year, month, day)
    hs = hn + datetime.timedelta(days=1)
    
    print("Ngay ke tiep la:", hs.strftime("%d/%m/%Y"))
except ValueError:
    print("Loi")
