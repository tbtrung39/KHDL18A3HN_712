#1
s=input("nhập chuỗi: ")
ds=s.replace(',', ' ').split()
for tu in ds:
    print(tu)
#2
s=input("nhập chuỗi: ")
tu=''
for c in s:
    if c!=' ' and c!=',':
        tu+=c
    else:
        if tu!="":
            print(tu)
            tu=""
if tu!="":
    print(tu)