#cach 1 
s=input("nhap chuoi: ")
ds=s.replace(',', ' ').split()
for tu in ds:
    print(tu)
#cach 2
s=input("nhap chuoi: ")
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