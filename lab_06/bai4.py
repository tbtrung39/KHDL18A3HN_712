numbers = []
while True:
    num = int(input("Nhập một số tự nhiên (hoặc nhập 0 để kết thúc): "))
    if num == 0:
        break
    numbers.append(num)
insert_list = [1, 2, 3]
numbers.insert(0, insert_list)  
numbers.append(insert_list)  
if len(numbers) >= 5:
    numbers.insert(5, insert_list) 
else:
    numbers.append(insert_list)  

print("Danh sách sau khi chèn:", numbers)

k = int(input("Nhập chỉ số k của phần tử muốn xóa: "))
if 0 <= k < len(numbers):
    del numbers[k]
    print(f"Danh sách sau khi xóa phần tử thứ {k}:", numbers)
else:
    print(f"Chỉ số {k} không hợp lệ.")


numbers.sort()  
print("Danh sách sau khi sắp xếp tăng dần:", numbers)

numbers.sort(reverse=True) 
print("Danh sách sau khi sắp xếp giảm dần:", numbers)