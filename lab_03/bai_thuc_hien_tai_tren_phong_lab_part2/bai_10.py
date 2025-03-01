n = int(input("Nhập số nguyên dương: "))
while n <= 0:
    n = int(input("Nhập lại số nguyên dương: "))
print("Phân tích thừa số nguyên tố của", n, "là: ", end="")
for i in range(2, n + 1):
    while n % i == 0:
        print(i, end=" ")
        n //= i
