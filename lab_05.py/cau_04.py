str1=input("nhập chuỗi 1: ")
str2=input("nhập chuỗi 2: ")
ket_qua=""
i=0
while i<len(str1) or i<len(str2):
    if i<len(str1):
        ket_qua+=str1[i]
    if i<len(str2):
        ket_qua+=str2[i]
    i+=1
print("chuỗi trộn là:", ket_qua)

