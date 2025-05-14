def tim_ucln(a, b):
    ucln = 1
    min_so = min(a, b)
    for i in range(1, min_so + 1):
        if a % i == 0 and b % i == 0:
            ucln = i
    return ucln
def tim_bcnn(a, b):
    ucln = tim_ucln(a, b)
    return abs(a * b) // ucln
def SumDivisor(n):
    tong = 0
    for i in range(1, n + 1):
        if n % i == 0:
            tong += i
    return tong
