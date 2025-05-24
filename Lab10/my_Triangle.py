import math
def ktra_tam_giac(a,b,c):
    return a+b>c and a+c>b and b+c>a
def chu_vi_tam_giac(a,b,c):
    if ktra_tam_giac(a,b,c):
        return a+b+c
    else:
        return None
def dien_tich_tam_giac(a,b,c):
    if ktra_tam_giac(a,b,c):
        p=(a+b+c)/2
        return math.sqrt(p*(p-a)*(p-b)*(p-c))
    else:
        return None