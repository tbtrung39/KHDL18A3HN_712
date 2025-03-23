Str=input("Nhập chuỗi ký tự:")
count=0
for char in Str:
    if not char.isalpha() and not char.isalnum():
        count+=1
print("Số ký tự không phải là tiếng anh là:",count)
