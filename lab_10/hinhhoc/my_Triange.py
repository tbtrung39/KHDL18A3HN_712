import math

def check_tam_giac(a, b, c):
    return a + b > c and a + c > b and b + c > a

def chu_vi_tam_giac(a, b, c):
    if check_tam_giac(a, b, c):
        return a + b + c
    else:
        return None

def dien_tich_tam_giac(a, b, c):
    if check_tam_giac(a, b, c):
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return s
    else:
        return None
