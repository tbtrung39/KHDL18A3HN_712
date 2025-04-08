# bai 16
a = list(map(int, input("Nhập dãy số, cách nhau bởi khoảng trắng: ").split()))
count = {}
so_cap = 0
for j in range(len(a)):
    x = a[j]
    if x - 1 in count:
        so_cap += count[x - 1]
    if x in count:
        count[x] += 1
    else:
        count[x] = 1
print("Số cặp (i, j) thỏa a[i] + 1 = a[j]:", so_cap)
