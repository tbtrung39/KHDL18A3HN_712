def s1(n): return 1 if n==1 else n+s1(n-1)
def s2(n): return 1 if n==1 else n**2 + s2(n-1)
try:
    n=int(input("nhap n: "))
    if n<=0: raise ValueError("n phai > 0")
    print(f"S1={s1(n)}\nS2={s2(n)}")
except ValueError as e:
    print("loi:",e)