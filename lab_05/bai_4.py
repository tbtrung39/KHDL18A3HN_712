Str1 = input("Nhap chuoi ky tu 1: ")
Str2 = input("Nhap chuoi ky tu 2: ")
kq = ""
i=0
while i<len(Str1) or i<len(Str2):
    if i<len(Str1):
        kq+=Str1[i]
    if i<len(Str2):
        kq+=Str2[i]
    i+=1
print("Chuoi da tron la: ", kq)