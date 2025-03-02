n = int(input("Nhập n: "))

print(f"Các số nguyên tố nhỏ hơn hoặc bằng {n} là:", end=" ")
for so in range(2, n + 1):
    la_nguyen_to = True
    for i in range(2, int(so ** 0.5) + 1):
        if so % i == 0:
            la_nguyen_to = False
            break
    if la_nguyen_to:
        print(so, end=" ")


