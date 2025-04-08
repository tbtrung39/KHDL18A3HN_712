a = list(map(int, input("Nhập dãy số nguyên cách nhau bằng khoảng trắng: ").split()))
n = len(a)
pairs = []

for i in range(n - 1):
    for j in range(i + 1, n):
        if a[i] + a[j] == a[i + 1]:
            pairs.append((i, j))

print("Các cặp chỉ số (i, j) thỏa điều kiện a[i] + a[j] = a[i+1]:")
print(pairs)
