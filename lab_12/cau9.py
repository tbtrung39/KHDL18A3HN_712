from datetime import datetime
days=['thu2','thu3','thu4','thu5','thu6','thu7','chu nhat']
try:
    date_str=input('nhap ngay')
    date= datetime.strptimr(date_str,'%d-%m_Y')
    print('ngay do lai:',days[date.weekday()])
except ValueError:
    print('ngay khong hop le')