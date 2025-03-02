n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Vui lòng nhập n > 0: "))
S1 = 0
S2 = 0
S3 = 0
for i in range(1, n+1):
    S1 += i
    S2 += (2*i - 1)
    S3 += 2*i
print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)