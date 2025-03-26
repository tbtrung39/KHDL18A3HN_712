str1=input("nhap chuoi ky tu 1: ")
str2=input("nhap chuoi ky tu 2: ")
#a)
print(str1+str2)

#b)
a=len(str1)
b=len(str2)
s=""
if a>=b:
    dai=a
else:
    dai=b
for i in range(dai):
    if i<a:
        s+=str1[i]
    if i<b:
        s+=str2[i]
print(s)