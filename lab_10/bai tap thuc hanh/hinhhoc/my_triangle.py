import math
def is_Tamgiac(a,b,c):
    return a+b>c and a+c>b and b+c>a

def Chu_vi_tam_giac(a,b,c):
    return a+b+c

def Dien_tich_tam_giac(a,b,c):
    if not is_Tamgiac(a,b,c):
        return None
    p=(a+b+c)/2
    return (p*(p*a)*(p-b)*(p-c))**0.5

