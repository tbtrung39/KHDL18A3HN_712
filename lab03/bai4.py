n=int(input("nhap so nguyen: "))

for i in range(1,n+1):
    c=1
    for j in range(2,i):
        if i==2:
            c=1
        else:
            if i%j==0:
                c=0
                break
    if c==1:
        print(i)
