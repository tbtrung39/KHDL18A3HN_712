#Bai14
so_nhi_phan={}
for i in range(1,101):
    n=i
    nhi_phan=""
    while n>0:
        nhi_phan=str(n%2) + nhi_phan
        n //= 2
    so_nhi_phan[i]=nhi_phan
print(so_nhi_phan)