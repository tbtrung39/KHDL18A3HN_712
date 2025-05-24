from datetime import datetime
def date_difference(date1,date2):
    delta=abs(date2-date1)
    return delta.days//365,(delta.days %365)//30,(delta.days%365)%30
try:
    date1_str=input('nhap ngay thu nhat')
    date2_str=input('nhap ngay thu hai')
    d1= datetime.strptime(date1_str,'%d=%m-%y')
    d2=datetime.strptime(date2_str,'%d=%m-%y')
    y,m,d= date_difference(d1,d2)
    print('khong cach nam thang ngay')
except ValueError:
    print('loi dinh dang ngay')