n = int(input("Nhập số nguyên dương: "))
if n <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    print("Phân tích thừa số nguyên tố:", end=" ")
    for i in range(2, n + 1):
        for _ in range(n // i + 1):
            if n % i == 0:
                print(i, end=" * " if n // i > 1 else "")
                n //= i
