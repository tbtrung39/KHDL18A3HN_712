n = int(input("Nhập số hàng của tam giác: "))

for i in range(n):
    print(" " * (n - i - 1), end="")
    if i == 0:
        print("*")
    elif i == n - 1:
        print("* " * (i + 1))
    else:
        print("*" + " " * (2 * i - 1) + "*")
