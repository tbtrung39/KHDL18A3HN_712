# cau 2
# cach 1
Str = input("Nhập chuỗi ký tự: ")
count = 0  
for char in Str:
    if not ('a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9'):
        count += 1  
print("Số ký tự không phải là chữ cái tiếng Anh và không phải là số:", count)
# cach 2
Str = input("Nhập chuỗi: ")
count = 0  
for char in Str:
    if not char.isalnum(): 
        count += 1
print("Số ký tự không phải là chữ cái tiếng Anh và không phải là số:", count)

