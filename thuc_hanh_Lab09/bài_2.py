def ucln(a, b):
    if b == 0:
        return a
    return ucln(b, a % b)
def ucln_n_so(n):
    x = int(input(f"Nhập số thứ {n}: "))
    if n == 1:
        return x
    else:
        return ucln(x, ucln_n_so(n - 1))
n = int(input("Nhập số lượng phần tử: "))
ket_qua = ucln_n_so(n)
print("Ước chung lớn nhất là:", ket_qua)
