str1=input("Nhập vào chuỗi ký tự")
tu="" 
for char in str1:
    if char.isalnum():
        tu += char
    else:
        if tu:
            print(tu)
            tu=""
if tu:
    print(tu)