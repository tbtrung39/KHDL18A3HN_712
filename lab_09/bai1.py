def lon_nhat(a, b):
    if a > b:
        return a
    else:
        return b

def lon_nhat_ba_so(x, y, z):
    return lon_nhat(x, lon_nhat(y, z))

so_1 = float(input("hay nhap so thu nhat: "))
so_2 = float(input("hay nhap so thu hai: "))
so_3 = float(input("hay nhap so thu ba tu ban phim: "))

kq = lon_nhat_ba_so(so_1, so_2, so_3)
print("So lon nhat trong 3 so la:", kq)