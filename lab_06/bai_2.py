n = int(input("Nhap so luong phan tu:"))
numbers = [int(input(f"Nnhap phan tu thu {i+1}:")) for i in range(n)]
sorted_numbers = sorted(set(numbers),reverse = True)
lon_thu_2 = sorted_numbers[1]
vi_tri_lon_thu_2 = numbers.index(lon_thu_2) if lon_thu_2 is not None else None

max_count = count=0
for num in numbers:
    if num > 0:
        count += 1
        max_count = max(max_count,count)
    else:
        count = 0

max_sum = current_sum = 0
count = 0
for num in numbers:
    if num > 0:
        current_sum += num
        max_sum = max(max_sum,current_sum)
    else:
        current_sum = 0
print("So lon thu hai:",lon_thu_2,"vị trí",vi_tri_lon_thu_2)
print("So luong so duong lien tiep gan nhat:",max_count)
print("Tong lon nhat cua day so duong lien tiep:",max_sum)