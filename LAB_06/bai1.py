a = [(2, 0), (4, 1), (19, 2), (-3, 3), (6, 4), 
     (3, 5), (-2, 6), (6, 7), (8, 8), (0, 9)]
sum_elements = sum(x[0] for x in a)
print("Tong cac phan tu:", sum_elements)
count_positive = sum(1 for x in a if x[0] > 0)
print("So luong so duong:", count_positive)
pos_first_negative = next((x[1] for x in a if x[0] < 0), -1)
print("Vi tri phan tu am dau tien:", pos_first_negative)
pos_last_positive = next((x[1] for x in reversed(a) if x[0] > 0), -1)
print("Vi tri phan tu duong cuoi cung:", pos_last_positive)
max_value, pos_max = max(a, key=lambda x: x[0])
print("Phan tu lon nhat:", max_value, "o vi tri:", pos_max)
min_value, pos_last_min = min(a, key=lambda x: (x[0], -x[1]))
print("Phan tu nho nhat cuoi cung:", min_value, "o vi tri:", pos_last_min)
