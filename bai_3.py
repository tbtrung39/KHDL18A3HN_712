import sohoc 
a = int(input("Hay nhap so nguyen a: "))
b = int(input("Hay nhap so nguyen b b: "))
n = int(input("Hay nhap so nguyen n n: "))
print("UCLN cua", a, "va", b, "la:", sohoc.Ucln(a, b))
print("BCNN cua", a, "va", b, "la:", sohoc.Bcnn(a, b))
print("Tong cac uoc cua", n, "la:", sohoc.SumDivisor(n))