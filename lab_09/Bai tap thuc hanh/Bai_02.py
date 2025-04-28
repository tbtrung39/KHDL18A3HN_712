def ucln(a, b):
    if b == 0:
        return a
    else:
        return ucln(b, a % b)

def ucln_cua_n_so(ds, n):
    if n == 1:
        return ds[0]
    else:
        return ucln(ds[n - 1], ucln_cua_n_so(ds, n - 1))

n = int(input("Nhập số lượng các số cần tính UCLN: "))
ds = []
for i in range(n):
    num = int(input(f"Nhập số thứ {i + 1}: "))
    ds.append(num)

result = ucln_cua_n_so(ds, n)
print(f"Ước chung lớn nhất của {n} số là: {result}")
