import my_Triange
a=float(input('nhap canh a:'))
b=float(input('nhap canh b:'))
c=float(input('nhap canh c:'))
if my_Triange.is_tamgiac(a,b,c):
    print('day la tam giac')
    print('chu vi tam giac',my_Triange.chuvitamgiac(a,b,c))
    print('dien tich tam giac',my_Triange.dientich_tamgiac(a,b,c))
else:
    print('ba canh khong tao thanh tam giac')