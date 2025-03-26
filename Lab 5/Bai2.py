#Bai2
#Cách 1
str = input("Nhập chuỗi ký tự: ") 
count = 0
for char in str:
    if not char.isalpha() and not char.isnumeric():
        count += 1
print("Số ký tự không phải là chữ cái tiếng Anh và không là số trong chuỗi:", count)
#Cách 2
s = input("Nhập chuỗi: ")
count = 0
for char in s:
    if not ('a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9'):
        count += 1
print("Số ký tự không phải là chữ cái tiếng Anh và không là số trong chuỗi:", count)