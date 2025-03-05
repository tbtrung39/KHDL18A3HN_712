n=int(input("nhap so nguyen n: "))
for i in range(1,n):
    s=0
    for j in range(1,i):
        if i%j==0:
            s+=j
    if s==i:
        print(i)