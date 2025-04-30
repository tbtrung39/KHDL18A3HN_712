#Bai2
def ucln(a, b):
    if b == 0:
        return a
    else:
        return ucln(b, a % b)
def ucln_cua_n_so(ds_so, n):
    if n == 1:
        return ds_so[0]
    else:
        return ucln(ds_so[n-1],ucln_cua_n_so(ds_so, n-1))
n = int(input("Nhập số lượng số cần tìm ucln: "))
ds_so = [int(input(f"nhap so thu {i+1}: ")) for i in range(n)]
kq = ucln_cua_n_so(ds_so, n)
print("Ước chung lớn nhất của",n,"số là:",kq)