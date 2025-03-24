# cau 1
str = input("Nhập chuỗi ký tự: ")
count = 0
for char in str:
    if char.isdigit():  
        count += 1
print("Số lượng ký tự là số trong chuỗi:", count)
