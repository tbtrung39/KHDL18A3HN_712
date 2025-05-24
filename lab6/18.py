# Nhập số bậc n từ bàn phím
n = int(input("Nhập bậc n của ma trận đơn vị: "))

# Tạo ma trận đơn vị bậc n
A = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

print("Ma trận đơn vị bậc", n, "là:")
for hang in A:
    print(hang)