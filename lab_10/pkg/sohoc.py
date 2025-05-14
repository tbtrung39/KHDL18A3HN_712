def Ucln(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def Bcnn(a,b):
    return abs(a*b)//Ucln(a,b)