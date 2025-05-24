def is_TamGiac(a,b,c):
    return a+b>c and a+c>b and b+c>a
def ChuViTamGiac(a,b,c):
    return a+b+c if is_TamGiac(a,b,c) else 0
def S_TamGiac(a,b,c):
    if not is_TamGiac(a,b,c): return 0
    p = (a+b+c)/2
    return (p*(p-a)*(p-b)*(p-c))** 0.5