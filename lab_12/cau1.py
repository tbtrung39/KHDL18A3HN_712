def sum1(n):
    if n==1:
        return 1
    return n+ sum1(n-1)
def sum2(n):
    if n==1:
        return 1
    return n**2 +sum2(n-1)
try:
    n=int(input('nhap so nguyen duong n:'))
    if n<=0:
        raise ValueError('n phai la so nguyen duong')
    print('s1=',sum1(n))
    print('s2=',sum2(n))
except ValueError as e:
    print('loi:',e)