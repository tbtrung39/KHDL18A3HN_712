n = int(input("Nhập số nguyên dương n: "))
if n <= 1:
    print("Vui lòng nhập số nguyên dương lớn hơn 1.")
else:
    print(f"{n} = ", end="")
    for i in range(2, n + 1):
        S = 0
        while n % i == 0:
            S += 1
            n //= i
        if S > 0:
            if S == 1:
                print(f"{i}", end="")
            else:
                print(f"{i}^{S}", end="")
            if n > 1:
                print(" * ", end="")
    if n == 1:
        print()
    else:
        print(f"{n}")