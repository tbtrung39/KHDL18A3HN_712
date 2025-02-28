n = int(input("Nhập số nguyên dương: "))
print(f"Phân tích thừa số nguyên tố của {n} là: ", end="")
if n % 2 == 0:
    print(2, end=" ")
    n //= 2
for i in range(3, int(n**0.5) + 1, 2):
    if n % i == 0:
        print(i, end=" ")
        n //= i
if n > 2:
    print(n)
