so = int(input("Nhập một số nguyên dương: "))
if so > 0:
    print("Phân tích thừa số nguyên tố:", end=" ")
    for i in range(2, so + 1):
        while so % i == 0:
            print(i, end=" ")
            so //= i
    print()
else:
    print("Vui lòng nhập một số nguyên dương!")