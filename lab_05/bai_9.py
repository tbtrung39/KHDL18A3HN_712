#Cách 1:
str=input("Nhap chuoi: ")
max_kt=str[0] if str else ''
max_len=1
hien_tai=str[0] if str else ''
dem=1
for i in range(1, len(str)):
    if str[i]==str[i-1]:
        dem+=1
        if dem>max_len:
            max_len=dem
            max_kt=str[i]
    else:
        dem=1
print(max_kt*max_len)

#Cách 2:
str=input("Nhap chuoi: ")
a,b,c='','',0
for i in str:
    c=c+1 if i==b else 1
    b=i
    if c>len(a): a=b*c
print(a)