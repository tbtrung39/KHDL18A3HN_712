def so_lon_nhat(a, b, c):
    def so_sanh(x, y):
        if x > y:
            return x
        else:
            return y
    return so_sanh(a, so_sanh(b, c))
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))
kq = so_lon_nhat(a, b, c)
print("So lon nhat trong 3 so la: ", kq)