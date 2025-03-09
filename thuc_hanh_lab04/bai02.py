import math
#a)
while True:
    n = int(input("Nhập số nguyên n là: "))
    if n > 0:
        break
    else:
        print("Vui lòng nhập lại n!")
S1 = 0
i = 1
while i <= n :
    S1 += ((-1) ** (i + 1)) * (1 / i) 
    i += 1
print("S1 là:",S1)
#b)
while True:
    n = int(input("Nhập số nguyên n là: "))
    if n > 0:
        break
    else:
        print("Vui lòng nhập lại n!")
S2 = 0
j = 1
while j <= n :
    S2 += 1/(j*(j+1))
    j += 1
print("S2 là: ",S2)
#c)
while True:
    n = int(input("Nhập số nguyên n là: "))
    if n >= 2:
        break
    else:
        print("Vui lòng nhập lại n!")
S3 = 0
k = 2
while k <= n :
    S3 += 1/ (math.sqrt(k))
    k += 1
print("Tổng S3 là:",S3)