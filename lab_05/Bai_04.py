str1=input("Nhập chuỗi ký tự thứ nhất:")
str2=input("Nhập chuỗi ký tự thứ hai:")
ket_qua=""
do_dai=max(len(str1),len(str2))
for i in range(do_dai):
    if i<len(str1):
        ket_qua += str1[i]
    if i<len(str2):
        ket_qua += str2[i]
print("Chuỗi sau khi trộn là:",ket_qua)