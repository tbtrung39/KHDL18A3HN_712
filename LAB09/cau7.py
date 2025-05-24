def timnghiem(N,n):
    if n==1:return[[N]]
    return [[x]+p for x in range(N+1) for p in timnghiem(N-x,n-1)]

N,n=map(int,input("Nhập N và n:").split())
print(timnghiem(N,n))
