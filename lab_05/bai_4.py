# Cách 1
Str1 = input("Nhap chuoi ky tu Str1: ")
Str2 = input("Nhap chuoi ky tu Str2: ")
ket_qua = ""
do_dai = max(len(Str1), len(Str2))
for i in range(do_dai):
    if i<len(Str1):
        ket_qua += Str1[i]
    if i<len(Str2):
        ket_qua += Str2[i]
print("Chuoi sau khi tron la: ", ket_qua)

# Cách 2
Str1 = input("Nhap chuoi ky tu Str1: ")
Str2 = input("Nhap chuoi ky tu Str2: ")
ket_qua = ""
i = 0
while i<len(Str1) or i<len(Str2):
    if i<len(Str1):
        ket_qua += Str1[i]
    if i<len(Str2):
        ket_qua += Str2[i]
    i += 1
print("Chuoi da tron la: ", ket_qua)