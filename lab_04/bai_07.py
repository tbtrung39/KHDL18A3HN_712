a = int(input('Nhập số nguyên a: '))
b = int(input('Nhập số nguyên b: '))
if a==0 or b==0:
    print('Không tồn tại BCNN vì một trong hai số bằng 0')
else:
    x,y = a,b
    while y!=0:
        x,y = y, x%y
    bcnn = abs(a*b)//x
    print(f'Bội chung nhỏ nhất của {a} và {b} là: {bcnn}')