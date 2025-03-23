#Cách 1
s = input("Nhập chuỗi ký tự: ")
count = 0
for i in "0123456789": 
    count += s.count(i)
print("Số lượng ký tự là số trong chuỗi:", count)
#Cách 2
s = input("Nhập chuỗi ký tự: ")  
count = 0  

for char in s:
    if char.isdigit():  
        count += 1

print("Số lượng ký tự là số trong chuỗi:", count)
