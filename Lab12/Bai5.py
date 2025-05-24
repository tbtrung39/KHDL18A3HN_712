def s1(n):
    if n<0:
        raise ValueError("Phai nhap so nguyen duong!")
    if n==0:
        return 0
    return n+s1(n-1)
def s2(n):
    if n<0:
        raise ValueError("Phai nhap so nguyen duong!")
    if n==0:
        return 0
    return n**2+s2(n-1)
try:
    n=int(input("Nhap n:"))
    print("S1=", s1(n))
    print("S2=", s2(n))
except ValueError as e:
    print("Loi:", e)