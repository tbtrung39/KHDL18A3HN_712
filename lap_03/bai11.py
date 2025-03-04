# Nhập số nguyên dương n làm độ rộng tam giác
n = int(input("Nhập số hàng của tam giác (n): "))

# Kiểm tra nếu n <= 0 thì yêu cầu nhập lại
while n <= 0:
    n = int(input("Vui lòng nhập số nguyên dương n: "))

print("\n(a) Tam giác vuông cân:")
for i in range(1, n + 1):
    if i == 1 or i == n:
        print("*" * i)
    else:
        print("" + " " * (i - 2) + "")

print("\n(b) Tam giác cân:")
for i in range(1, n + 1):
    spaces = n - i  # Số khoảng trắng trước dấu sao
    if i == 1:
        print(" " * spaces + "*")
    elif i == n:
        print("*" * (2 * n - 1))
    else:
        print(" " * spaces + "" + " " * (2 * i - 3) + "")

print("\n(c) Tam giác úp ngược:")
for i in range(n, 0, -1):
    spaces = n - i  # Số khoảng trắng trước dấu sao
    if i == 1:
        print(" " * spaces + "*")
    elif i == n:
        print("*" * (2 * n - 1))
    else:
        print(" " * spaces + "" + " " * (2 * i - 3) + "")