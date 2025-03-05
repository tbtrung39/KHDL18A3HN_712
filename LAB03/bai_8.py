#phan a
n = int(input("nhập số nguyên dương:"))
if n <= 0:
    print("không hợp lệ vui lòng nhập lại")

else:
    S1 = 0
    for i in range(1,n+1):
        S1 += i
    S2 = 0
    for i in range(1,2*n + 2,2):
        S2 += i
    S3 = 0
    for i in range(2,n**2 + 1,2):
        S3 += i
    print(f"S1 = 1 + 2 + 3 + ... +{n}=",S1)
    print(f"S2 = 1 + 3 + 5 + ... + ({n}*2 + 1)=",S2)
    print(f"S3 = 2 + 4 + 6 + ... + ({n}*2)=",S3)
