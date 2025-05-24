def hv(a,k):
    if k==len(a): print(*a)
    else:
        for i in range(k,len(a)):
            a[k],a[i]=a[i],a[k]
            hv(a,k+1)
            a[k],a[i]=a[i],a[k]

n=int(input("Nhập số tự nhiên n: "))
hv(list(range(1,n+1)),0)