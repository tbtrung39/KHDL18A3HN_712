# cau 12
# cach 1
str1=input("Hay nhap chuoi ky tu: ")
tu_hien_tai = ""
for char in str1:
    if char.isalpha():
        tu_hien_tai += char
    else:
        if tu_hien_tai:
            print(tu_hien_tai)
            tu_hien_tai = ""
if tu_hien_tai:
    print(tu_hien_tai)
# cach 2
str1=input("Hay nhap chuoi ky tu: ")
tu_hien_tai = ""
i=0
while i < len(str1):
    char = str1[i]
    if char != ' ' and char != ',':
        tu_hien_tai += char
    else:
        if tu_hien_tai != "":
            print(tu_hien_tai)
            tu_hien_tai = ""
    i += 1
if tu_hien_tai != "":
    print(tu_hien_tai)
