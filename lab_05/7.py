str=input("nhap chuoi: ")
a=""
for i in str:
    if i.isdigit():
        a+=i
a=int(a)
s=0
for i in range(1,a-1):
    if a%i==0:
        s+=i
if s==a:
    print("chuoi so la so hoan hao")
else:
    print("chuoi so khong phai so hoan hao")