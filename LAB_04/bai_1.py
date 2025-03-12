while True:
    n = int(input("nhập giá trị của n:"))
    if n<0:
        break
    s1 = 0
    i = 1
    while i <= n:
       s1 += i**2
       i += 1
    s2 = 0
    i = 1
    while i <= (2*n+1):
       s2 += i**3
       i += 2
    s3 = 0
    i = 1
    while i <= (2*n):
       s3 += i**4
       i += 2
    print(f"S1={s1}")
    print(f"S2={s2}")
    print(f"S3={s3}")
