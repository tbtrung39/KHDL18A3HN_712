n = int(input("Nhap so phan tu: "))
a = [(int(input(f"Nhap phan tu thu {i + 1}: ")), i) for i in range(n)]
max_sum, cur_sum = float('-inf'), 0
start, end, temp_start = 0, 0, 0
for i, (value, _) in enumerate(a):
    if cur_sum <= 0:
        cur_sum = value
        temp_start = i
    else:
        cur_sum += value
    if cur_sum > max_sum:
        max_sum = cur_sum
        start, end = temp_start, i
print("Tong lon nhat:", max_sum)
print("Mang con co tong lon nhat:", [x[0] for x in a[start:end + 1]])
