import math
n=int(input("Nhập số nguyên dương n: "))
while n<=0:
    n=int(input("Vui lòng nhập lại n là số nguyên dương: "))
tongS1=0
tongS2=0
tongS3=0
i=1
while i<=n:
    if i%2==0:
        tongS1-=1/i
    else:
        tongS1+=1/i
    i+=1
i=2
while i<=n:
    tongS2+=1/(i*(i+1))
    i+=1
i=2
while i<=n:
    tongS3+=1/math.sqrt(i)
    i+=1
print("Tổng S ở ý a) là:", tongS1)
print("Tổng S ở ý b) là:", tongS2)
print("Tổng S ở ý C) là:", tongS3)