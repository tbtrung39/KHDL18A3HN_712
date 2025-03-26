Str1 = input("Nhập chuỗi thứ nhất: ")
Str2 = input("Nhập chuỗi thứ hai: ")
chuoi_tron = ""
max_len = max(len(Str1), len(Str2))
for i in range(max_len):
    if i < len(Str1):
        chuoi_tron += Str1[i]
    if i < len(Str2):
        chuoi_tron += Str2[i]
print("Chuỗi sau khi trộn:", chuoi_tron)
