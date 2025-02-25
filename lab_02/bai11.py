ngay = int(input('Nhập ngày: '))
thang = int(input('Nhập tháng: '))
nam = int(input('Nhập năm: '))
if 1 <= thang <= 12:
    if 1 <= ngay <= 31:
        if thang == 2:
            if nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0):
                if ngay < 29:
                    ngay += 1
                else:
                    ngay = 1
                    thang += 1
            else:
                if ngay < 28:
                    ngay += 1
                else:
                    ngay = 1
                    thang += 1
        elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
            if ngay < 30:
                ngay += 1
            else:
                ngay = 1
                thang += 1
        else:
            if ngay < 31:
                ngay += 1
            else:
                ngay = 1
                if thang < 12:
                    thang += 1
                else:
                    thang = 1
                    nam += 1
        print(f'Ngày tiếp theo: {ngay}/{thang}/{nam}')
    else:
        print('Ngày không hợp lệ')
else:
    print('Tháng không hợp lệ')
