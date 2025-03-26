#cách 1
s=input("nhap chuoi: ")
d=0
for k in s:
    if k.isdigit():
        d+=1
print("so chu so la:", d)
#cách 2
s=input("nhap chuoi: ")
d=0
for k in s:
    d+=1 if '0' <=k<='9' else 0
print("so chu so la:", d)