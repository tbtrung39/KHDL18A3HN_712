str = input("Nhap chuoi ky tu: ")
so_str=" "
for i in str:
    if i.isdigit():
        so_str+=i
if so_str==" ":
    print("Khong co so nao trong chuoi.")
else:
    n=int(so_str)
    print("So lay duoc la:", n)
    tong=0
    for j in range(1,n):
        if n%j == 0:
            tong+=j
    if tong == n:
        print(n, "la so hoan hao")
    else:
        print(n, "khong la so hoan hao")