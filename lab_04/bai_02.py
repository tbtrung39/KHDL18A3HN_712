while True:
    n = int(input("Nhập vào số nguyên dương n: "))
    if n > 0:
        break
    else:
        print("Nhập sai, mời nhập lại!")
#a)
i = 1
S1 = 0
while i <= n:
    if i % 2 == 0:
        S1 -= 1/i
    else:
        S1 += 1/i
    i += 1
print("S1 =", S1)
#b)
i = 2
S2 = 0
while  i <= n + 1:
    S2 += 1 / (i * (i+1))
    i += 1
print("S2 =", S2)

#c)
i = 2
S3 = 0
while i <= n:
    S3 += 1 / (i**(1/2))
    i += 1
    print("S3 =", S3)

