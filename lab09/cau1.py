def so_lon_nhat(a,b,c):
    def so_sanh(x,y):
        if x>y:
            return x
        else:
            return y
    return so_sanh(a,so_sanh(b,c))

a=float(input("nhap a: "))
b=float(input("nhap b: "))
c=float(input("nhap c: "))
kq=so_lon_nhat(a,b,c)
print("so lon nhat trong 3 so la: ",kq)