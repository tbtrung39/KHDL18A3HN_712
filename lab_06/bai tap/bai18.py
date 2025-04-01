m, n = map(int, input("Nhập số hàng và số cột (cách nhau bởi dấu phẩy): ").split(","))
matrix = []

print("Nhập ma trận:")
for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

total_sum = sum(sum(row) for row in matrix)

print("\nMa trận đã nhập:")
for row in matrix:
    print(row)

print("\nTổng các phần tử của ma trận:", total_sum)
