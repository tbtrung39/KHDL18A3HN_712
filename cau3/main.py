import sohoc
a = int(input('nhap so nguyen a'))
b = int(input('nhap so nguyen b'))
n = int(input('nhap so nguyen n'))
print("UCLN cua", a, "va", b, "la:", sohoc.Ucln(a, b))
print("BCNN cua", a, "va", b, "la:", sohoc.Bcnn(a, b))
print("Tong cac uoc cua", n, "la:", sohoc.SumDivisor(n))
