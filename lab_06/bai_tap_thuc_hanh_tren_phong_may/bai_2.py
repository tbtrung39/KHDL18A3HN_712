n=int(input("Nhập số lượng phần tử:"))
numbers=[int(input(f"Nhập phần tử thứ {i+1}:")) for i in range(n)]
sorted_numbers=sorted(set(numbers),reverse=True)
lon_thu_2=sorted_numbers[1]
vi_tri_lon_thu_2=numbers.index(lon_thu_2) if lon_thu_2 is not None else None

max_count=count=0
for num in numbers:
    if num >0:
        count += 1
        max_count=max(max_count,count)
    else:
        count=0

max_sum=current_sum=0
count=0
for num in numbers:
    if num >0:
        current_sum += num
        max_sum=max(max_sum,current_sum)
    else:
        current_sum=0
print("Số lớn thứ hai:", lon_thu_2, "vị trí",vi_tri_lon_thu_2)
print("Số lượng số dương liên tiếp nhiều nhất: ",max_count)
print("Tổng lớn nhất của dãy số dương liên tiếp: ",max_sum)