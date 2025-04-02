numbers = []
while True:
    n = int(input("Nhap so 0 de dung:"))
    if n == 0:
        break
    numbers.append(n)
    
insert_list = [1, 2, 3]
numbers = [1,2,3] + numbers
numbers += [1,2,3]
if len(numbers) >= 5:
    numbers = numbers[:4] + [1,2,3] + numbers[4:]
print("Danh sach sau khi chen:", numbers)

k = int(input("Nhap vi tri can xoa:"))
if 0 <= k < len(numbers):
    numbers.pop(k)
else: 
    print("Vi tri khong hop le.")

numbers.sort()
print("Danh sach sau khi sap xep tang dan:", numbers)
numbers.sort(reverse = True) 
print("Danh sach sau khi sap xep giam dan:", numbers)
