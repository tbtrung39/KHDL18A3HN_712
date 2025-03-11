n=int(input("Nhập số nguyên dương: "))
while n<=0:
    n=int(input("Vui lòng nhập lại số nguyên dương n: "))
s4=0
s5=0
s6=0
i=1
while i<=n:
    s4+=i**2
    i+=1
i=1
dem=0
while dem<n:
    s5+=i**3
    i+=2
    dem+=1
i=2
dem=0
while dem<n:
    s6+=i**4
    i+=2
    dem+=1
print(s4)
print(s5)
print(s6)
