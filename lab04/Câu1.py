n=int(input("Nhập số nguyên dương: "))
while n<=0:
    n=int(input("Vui lòng nhập lại số nguyên dương n: "))
tongS4=0
tongS5=0
tongS6=0
i=1
while i<=n:
    tongS4+=i**2
    i+=1
i=1
dem=0
while dem<n:
    tongS5+=i**3
    i+=2
    dem+=1
i=2
dem=0
while dem<n:
    tongS6+=i**4
    i+=2
    dem+=1
print("Tổng S4=", tongS4)
print("Tổng S5=", tongS5)
print("Tổng S6=", tongS6)
