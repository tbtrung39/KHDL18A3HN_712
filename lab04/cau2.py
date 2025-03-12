#a)
while True:
    n=int(input("nhập số nguyên dương: "))
    if n<=0:
        print("nhập sai yêu cầu, vui lòng nhập lại")
    else:
        s1=1
        i=1
        while i<=n:
            if i%2!=0:
                s1+=(-1/i)
                i+=1
            else:
                s1+=(1/i)
                i+=1
        print(s1)
        break

#b)
while True:
    n=int(input("nhập số nguyên dương: "))
    if n<=0:
        print("nhập sai yêu cầu, vui lòng nhập lại")
    else:
        s2=0
        i=1
        while i<=n:
            s2+=1/(i*(i+1))
            i+=1
        print(s2)
        break

#c)
while True:
    n=int(input("nhập số nguyên dương: "))
    if n<=0:
        print("nhập sai yêu cầu, vui lòng nhập lại")
    else:
        s3=0
        i=2
        while i<=n:
            s3+=1/(i**(1/2))
            i+=1
        print(s3)
        break