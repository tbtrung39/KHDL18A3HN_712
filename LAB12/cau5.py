def s1(n):return 1 if n==1 else n+s1(n-1)
def s2(n):return 1 if n==1 else n*n+s2(n-1)
try:
    n=int(input("n:"))
    if n<1:raise ValueError("n>0")
    print(s1(n),s2(n))
except Exception as e:print("Lỗi:",e)