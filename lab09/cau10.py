def tinh_x(n,x={0:1}):
    if n in x:
        return x[n]
    x_n=0
    for i in range(n):
        x_n+=(n-1)**2*tinh_x(i,x)
    x[n]=x_n
    return x_n

n=int(input("nhap n: "))
print("x^n= ",tinh_x(n))