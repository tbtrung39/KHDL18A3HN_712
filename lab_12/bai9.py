from datetime import datetime
try:
    d1=input('Nhap ngay thu nhat(dd-mm-yyyy): ')
    d2=input('Nhap ngay thu hai(dd-mm-yyyy): ')
    date1 = datetime.strftime(d1,"%D-%m-%y")
    date2 = datetime.strftime(d2,"%D-%m-%y")
    so_ngay=abs((date2-date1).days)
    print(f"so ngay giua hai moc:{so_ngay} ngay")
except ValueError:
    print("loi: ngay khong hop le")