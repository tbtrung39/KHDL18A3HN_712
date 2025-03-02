n = int(input("Nhập số nguyên dương: "))
while n <= 0:
    n = int(input("Vui lòng nhập số nguyên dương: "))
i = 2
print("Thừa số nguyên tố:", end=" ")
first = True
while n > 1:
    if n % i == 0:
        if not first:
            print("*", end=" ")
        print(i, end=" ")
        first = False
        n //= i
    else:
        i += 1
print()
