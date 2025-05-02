def ucln(a, b):
    if b == 0:
        return a
    return ucln(b, a % b)
def ucln_n(so, index = 0):
    if index == len(so) - 1:
        return so[index]
    return ucln(so[index], ucln_n(so, index + 1))
    
n = int(input("Nhap so luong so nguyen: "))
so = []
for i in range(n):
    x = int(input(f"Nhap so thu {i + 1}: "))
    so.append(x)
kq = ucln_n(so)
print("UCLN cua cac so la: ", kq)