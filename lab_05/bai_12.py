#Cách 1:
str1=input("Nhap chuoi ky tu: ")
ds=str1.replace(',', ' ').split()
for tu in ds:
    print(tu)

#Cách 2:
str1=input("Nhap chuoi ky tu: ")
tu=''
for i in str1:
    if i!=' ' and i!=',':
        tu+=i
    else:
        if tu!="":
            print(tu)
            tu=""
if tu!="":
    print(tu)