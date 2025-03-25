#cách 1
s=input("nhập chuỗi: ")
d=0
for k in s:
    if k.isdigit():
        d+=1
print("số chữ số là:", d)
#cách 2
s=input("nhập chuỗi: ")
d=0
for k in s:
    d+=1 if '0' <=k<='9' else 0
print("số chữ số là:", d)