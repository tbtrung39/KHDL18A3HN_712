n = int(input("Nhập số nguyên dương: "))

if n <= 0:
    print("Vui lòng nhập số nguyên dương!")
else:
    print("Phân tích thừa số nguyên tố của", n, "là:", end=" ")
    while n % 2 == 0:
        print(2, end=" ")
        n //= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            print(i, end=" ")
            n //= i
        i += 2
    if n > 1:
        print(n)
