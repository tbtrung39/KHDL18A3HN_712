import math
def is_TamGiac(a,b,c):
    if (a + c) > b and (a + b) > c and (c + b) > a:
        return True
    else:
        return False
    
def ChuviTamGiac(a,b,c):
    cv = a + b + c
    return cv
    
def S_TamGiac(a,b,c):
    p = (a + b + c)/2
    S = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return S

    