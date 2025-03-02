n = int(input("Nhập số hàng: "))

for i in range(n):
    if i == 0:
        print(" " * (n - i - 1) + "*")
    elif i == n - 1:
        print("*" * (2 * i + 1))
    else:
        print(" " * (n - i - 1) + "*" + " " * (2 * i - 1) + "*")
print()  

for i in range(n - 1):
    if i == 0:
        print(" " * (n - 1) + "*")
    else:
        print(" " * (n - i - 1) + "*" + " " * (2 * i - 1) + "*")
print("* " * n)  

print()  


for i in range(n):
    print(" " * (n - i - 1) + "* " * (i + 1))
