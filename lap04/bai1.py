while True:
    try:
        n = int(input("Nhập một số nguyên dương n: "))
        if n > 0:
            break
        else:
            print("Vui lòng nhập một số nguyên dương!")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ!")
S4 = 0
i = 1
while i <= n:
    S4 += i**2
    i += 1
S5 = 0
i = 1
count = 0
while count < n:
    S5 += i**3
    i += 2
    count += 1
S6 = 0
i = 2
count = 0
while count < n:
    S6 += i**4
    i += 2
    count += 1

# Xuất kết quả
print("Tổng S4 =", S4)
print("Tổng S5 =", S5)
print("Tổng S6 =", S6)