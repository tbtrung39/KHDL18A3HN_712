import datetime

try:
    day = int(input("Nhap ngay: "))
    month = int(input("Nhap thang: "))
    year = int(input("Nhap nam: "))
    
    date = datetime.date(year, month, day)
    week_number= date.isocalendar()[1]
    
    print(f"Ngay {date.strftime("%d/%m/%Y")} thuoc tuan thu {week_number} cua nam {year}")
    
except ValueError:
    print("Loi")