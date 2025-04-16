import math
n=int(input("Nhập số nguyên dương n: "))
while n<=0:
    n=int(input("Vui lòng nhập lại n là số nguyên dương: "))
s1=0
s2=0
s3=0
i=1
while i<=n:
    if i%2==0:
        s1-=1/i
    else:
        s1+=1/i
    i+=1
i=2
while i<=n:
    s2+=1/(i*(i+1))
    i+=1
i=2
while i<=n:
    s3+=1/math.sqrt(i)
    i+=1
print(s1)
print(s2)
print(s3)