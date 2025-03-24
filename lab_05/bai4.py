# cau 4
Str1 = input("Nhập chuỗi thứ nhất: ")
Str2 = input("Nhập chuỗi thứ hai: ")
kq = ""
max_len = max(len(Str1), len(Str2))
for i in range(max_len):
    if i < len(Str1):  
        kq += Str1[i]
    if i < len(Str2):  
        kq += Str2[i]
print("Hai chuỗi sau khi trộn là:", kq)
