thang = int(input('Nhap thang: '))
if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
    ngay = 31
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    max_day = 30
elif thang == 2:
    max_day = 28
else:
    print('Vui lòng nhập lại')
print(thang,'có',ngay,'ngàyngày')