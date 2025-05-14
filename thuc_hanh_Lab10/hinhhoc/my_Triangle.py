def la_tam_giac(a, b, c):
    return a + b > c and a + c > b and b + c > a
def ChuviTamGiac(a, b, c):
    if la_tam_giac(a, b, c):
        return a + b + c
    else:
        return "Không phải tam giác"
def S_TamGiac(a, b, c):
    if la_tam_giac(a, b, c):
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c))**0.5
    else:
        return "Không phải tam giác"
