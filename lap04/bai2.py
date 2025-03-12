while True:
    try:
        n = int(input("Nhập một số nguyên dương n: "))
        if n > 0:
            break
        else:
            print("Vui lòng nhập một số nguyên dương!")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ!")
S1 = 0
i = 1
while i <= n:
    if i % 2 == 0:
        S1 -= 1/i
    else:
        S1 += 1/i
    i += 1
S2 = 0
i = 1
while i <= n:
    S2 += 1 / (i * (i + 1))
    i += 1
S3 = 0
i = 2
while i <= n:
    S3 += 1**i
    i += 1
print("Tổng S1 =", S1)
print("Tổng S2 =", S2)
print("Tổng S3 =", S3)