n = int(input("Nhập độ rộng tam giác: "))
while n <= 0:
    n = int(input("Vui lòng nhập số nguyên dương: "))
for i in range(n, 0, -1):
    print(" " * (n - i), end="")