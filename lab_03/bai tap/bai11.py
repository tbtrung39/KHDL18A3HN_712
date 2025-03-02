n = int(input("Nhập độ rộng tam giác: "))
while n <= 0:
    n = int(input("Vui lòng nhập số nguyên dương: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    if i == 1 or i == n:
        print("*" * (2 * i - 1))
    else:
        print("*" + " " * (2 * i - 3) + "*")
print()