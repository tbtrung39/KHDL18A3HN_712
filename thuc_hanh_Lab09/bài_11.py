def giai_thua_kep(n):
    if n == 0 or n==1:
        return 1
    return n*giai_thua_kep(n-2)
def tinh_S(k):
    s=0
    for i in range(1,k+1):
        sign= -1 if i%2 == 0 else 1
        s += sign * giai_thua_kep(i)
    return s
k=int(input('Nhập k(k<1000):'))
print("Tổng S là:",tinh_S(k))
