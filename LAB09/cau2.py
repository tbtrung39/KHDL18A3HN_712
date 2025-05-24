def ucln(a,b):
    return a if b==0 else ucln(b,a%b)

def ucln_n(ds,n):
    return ds[0] if n==1 else ucln(ds[n-1],ucln_n(ds,n-1))

n=int(input('Nhập n: '))
ds=list(map(int,input(f"nhập {n} số cần tìm ước chung lớn nhất của {n} số đó (cách nhau bởi khoảng cách): ").split()))
while len(ds)!=n: ds=list(map(int,input(f'số lượng nhập không đúng, vui lòng nhập {n} số: ').split()))
print(ucln_n(ds,n))
