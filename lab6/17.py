# Nhập giá trị X và Y từ bàn phím
X = int(input("Nhập X: "))
Y = int(input("Nhập Y: "))

# Tạo mảng 2 chiều với giá trị i * j
mang_2_chieu = [[i * j for j in range(Y)] for i in range(X)]

for hang in mang_2_chieu:
    print(hang)