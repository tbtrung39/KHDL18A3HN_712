n=int(input("Nhập một số tự nhiên n: "))
A,B=set(),set()
for x in range(2,n):
    ngto=True
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            ngto=False
            break
    if ngto:
        if n%x==0:A.add(x)
        else:B.add(x)
print(f"Tập hợp A: {A}")
print(f"Tập hợp B: {B}")
