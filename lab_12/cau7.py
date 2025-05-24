from datetime import datetime
try:
    date_str=input('nhap ngay(dd-mm-yyyy):')
    date=datetime.strptime(date_str,"%d-%m-%Y")
    print('ngay hop le:',date,date)
except ValueError:
    print('ngay khong hop le')