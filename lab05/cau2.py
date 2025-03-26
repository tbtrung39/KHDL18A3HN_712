#cách 1
s=input('nhap chuoi: ')
d=0
for k in s:
    if not (k.isalpha() or k.isdigit()):
        d+=1
print("so ki tu khong la chu cai va khong la so la:", d)
#cach 2
s=input('nhap chuoi: ')
d=0
for k in s:
    ma=ord(k)
    if not (48<=ma<=57 or 65<=ma<=90 or 97<=ma<=122):
        d+=1
print("so ki tu khong phai chu cai va khong la so:", d)