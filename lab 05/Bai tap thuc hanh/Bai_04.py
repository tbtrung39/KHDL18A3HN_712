Str1=input("Nhập chuỗi ký tự thứ nhất:")
Str2=input("Nhập chuỗi ký tự thứ hai:")
ket_qua=""
do_dai=max(len(Str1),len(Str2))
for i in range(do_dai):
    if i<len(Str1):
        ket_qua += Str1[i]
    if i<len(Str2):
        ket_qua += Str2[i]
print("Chuỗi sau khi trộn là:",ket_qua)