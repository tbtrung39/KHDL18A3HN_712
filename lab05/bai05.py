s=input("nhap chuoi ki tu: ")
so_str=''
for k in s:
    if k.isdigit():
        so_str+=k
if so_str=='':
    print("khong co so nao trong chuoi")
else:
    n=int(so_str)
    print("so lay duoc la:", n)
    tong=0
    for i in range(1,n):
        if n%i==0:
            tong+=i
    if tong==n:
        print(n, "la so hoan hao")
    else:
        print(n, "khong la so hoan hao")