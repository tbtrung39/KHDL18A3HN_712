import math
def is_tamgiac(a,b,c):
    return a+b>c and a+c>b and b+c>a
def chuvitamgiac(a,b,c):
    if is_tamgiac (a,b,c):
        return a+b+c
    else:
        return 'khong phai tam giac'
def dientich_tamgiac(a,b,c):
    if is_tamgiac(a,b,c):
        p=(a+b+c)/2
        return math.sqrt(p*(p-a)*(p-b)*(p-c))
    else:
        return 'khong phai tam giac'
    