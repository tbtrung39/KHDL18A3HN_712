#Bai1
str = input("Nhập chuỗi ký tự: ")
count = 0
for char in str:
    if char.isnumeric():
        count += 1
print("Số ký tự là số trong chuỗi:", count)