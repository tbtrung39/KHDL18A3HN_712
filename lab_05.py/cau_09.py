#cách 1
s=input("nhập chuỗi: ")
max_kt=s[0] if s else ''
max_len=1
hien_tai=s[0] if s else ''
dem=1
for i in range(1, len(s)):
    if s[i]==s[i-1]:
        dem+=1
        if dem>max_len:
            max_len=dem
            max_kt=s[i]
    else:
        dem=1
print(max_kt*max_len)
#cách 2
s=input("nhập chuỗi: ")
m,c,t='','',0
for i in s:
    t=t+1 if i==c else 1
    c=i
    if t>len(m): m=c*t
print(m)