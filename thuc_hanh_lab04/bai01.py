#a)
while True:
    n = int(input("Nhập số nguyên dương n là: "))
    if n>0:
        break
    else:
        print("Vui lòng nhập lại n!")
S4 = 0
i = 1
while i <= n :
    S4 += i**2
    i += 1
print("Tổng của S4 là:",S4)
#b)
while True:
    n = int(input("Nhập số nguyên dương n là: "))
    if n>0:
        break
    else:
        print("Vui lòng nhập lại n!")
S5 = 0
j = 1
dem = 0
while dem < n :
    S5 += j**3
    j += 2
    dem += 1
print("Tổng của S5 là: ",S5)
#c)
while True:
    n = int(input("Nhập số nguyên dương n là: "))
    if n>0:
        break
    else:
        print("Vui lòng nhập lại n!")
S6 = 0
k = 2
dem = 0
while dem < n :
    S6 += k**4
    k += 2
    dem += 1
print("Tổng của S6 là: ",S6)