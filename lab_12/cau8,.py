from datetime import datetime,timedelta
date_str=input('nhap ngay(dd-mm-yyyy)')
try:
    date=datetime.strptime(date_str,'%d-%m-%Y')
    prev_day=date-timedelta(days=1)
    print('ngay truoc do:',prev_day.strftime('%d-%m-%y'))
except ValueError:
    print('loi dinh dang ngay')