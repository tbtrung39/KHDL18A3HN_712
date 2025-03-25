Str=input("Nhập chuỗi ký tự:")
so=0
for i in Str:
    if not i.isalpha() and not i.isalnum():
        so+=1
print("Số ký tự không phải là tiếng anh là:",so)