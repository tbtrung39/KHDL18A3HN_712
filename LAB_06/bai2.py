n = int(input("Nhap so phan tu: "))
a = [(int(input(f"Nhap phan tu thu {i + 1}: ")), i) for i in range(n)]
sorted_a = sorted(a, key=lambda x: x[0], reverse=True)
max2_value, max2_pos = sorted_a[1] if len(sorted_a) > 1 else (None, None)
print("Phan tu lon thu hai:", max2_value, "o vi tri:", max2_pos)
max_count, count = 0, 0
for value, _ in a:
    if value > 0:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0
print("So luong so duong lien tiep nhieu nhat:", max_count)
max_zero_count, zero_count = 0, 0
for value, _ in a:
    if value == 0:
        zero_count += 1
        max_zero_count = max(max_zero_count, zero_count)
    else:
        zero_count = 0
print("So luong so 0 lien tiep lon nhat:", max_zero_count)
