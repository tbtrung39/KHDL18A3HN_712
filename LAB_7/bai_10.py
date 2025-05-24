from datetime import datetime
d1 = datetime.strptime(input("Nhập ngày thứ nhất (dd-mm-yyyy): "), "%d-%m-%Y")
d2 = datetime.strptime(input("Nhập ngày thứ hai (dd-mm-yyyy): "), "%d-%m-%Y")

if d2 < d1:
    d1, d2 = d2, d1

delta = d2 - d1
total_days = delta.days

years = total_days // 365
months = (total_days % 365) // 30
days = (total_days % 365) % 30

print(f"Khoảng cách là: {years} năm, {months} tháng, {days} ngày.")