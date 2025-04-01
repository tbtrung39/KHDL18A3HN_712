n = int(input("Nhập số lượng phần tử: "))
a = []
print("Nhập các phần tử của danh sách:")
for i in range(n):
    x = int(input(f"Phần tử thứ {i + 1}: "))
    a.append(x)
if len(set(a)) < 2:
    print("Danh sách không có phần tử lớn thứ hai.")
else:
    max1 = max(a)  
    max2 = None   
    for x in a:
        if x != max1 and (max2 is None or x > max2):
            max2 = x
    vi_tri_max2 = len(a) - 1 - a[::-1].index(max2)
    print(f"Phần tử lớn thứ hai là {max2} tại vị trí {vi_tri_max2}.")

max_count = 0
count = 0
for x in a:
    if x > 0:
        count += 1
        if count > max_count:          
            max_count = count
    else:
        count = 0
print(f"Số lượng số dương liên tiếp nhiều nhất: {max_count}")

max_sum = 0
max_length = 0
current_sum = 0
current_length = 0
for x in a:
    if x > 0:
        current_sum += x
        current_length += 1
        if current_sum > max_sum:
            max_sum = current_sum
            max_length = current_length
    else:
        current_sum = 0
        current_length = 0
print(f"Số lượng số dương liên tiếp có tổng lớn nhất: {max_length}")