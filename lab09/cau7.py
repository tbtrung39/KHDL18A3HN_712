def day_nghiem(N,n,x=[],tong=0):
    if len(x)==n:
        if tong==N:
            print(x)
        return
    for i in range(N-tong+1):
        day_nghiem(N,n,x+[i],tong+i)

N=int(input("nhap so tu nhien N: "))
n=int(input("nhap so tu nhien n: "))
day_nghiem(N,n)