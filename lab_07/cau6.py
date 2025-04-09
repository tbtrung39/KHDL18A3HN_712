n=int(input("nhập n: "))
snt,x=[],2
while len(snt)<n:
    chia=False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            chia=True
            break
    if not chia:snt.append(x)
    x+=1
print(snt)
