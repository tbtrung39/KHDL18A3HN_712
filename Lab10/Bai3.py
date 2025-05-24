import sohoc
a=int(input("Nhap so nguyen a:"))
b=int(input("Nhap so nguyen b:"))
print("Uoc chung lon nhat cua a va b la:", sohoc.Ucln(a,b))
print("Boi chung nho nhat cua a va b la:", sohoc.Bcnn(a,b))
n=int(input("Nhap so nguyen n de tinh tong cac uoc:"))
print("Tong cac uoc cua",n,"la:", sohoc.SumDivisor(n))