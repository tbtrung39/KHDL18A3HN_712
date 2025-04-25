# bai 2
def ucln(a, b):
    if b == 0:
        return a
    else:
        return ucln(b, a % b)

def ucln_cua_n_so(danh_sach_so, n):
    if n == 1:
        return danh_sach_so[0]
    else:
        return ucln(danh_sach_so[n-1], ucln_cua_n_so(danh_sach_so, n-1))


n = int(input("nhap so luong cac so can tim ucln: "))
danh_sach_so = [int(input(f"nhap so thu {i+1}: ")) for i in range(n)]
kq = ucln_cua_n_so(danh_sach_so, n)

print(f"uoc chung lon nhat cua {n} so la: {kq}")
