str=input("nhap chuoi nhi phan:")
s=1
for i in str:
    if i=="1" or i=="0":
        s=1
    else:
        s=0
if s==1:
    b=int(str,2)     
    print("doi tu he nhi phan sang thap phan", b)
else:
    print("nhap sai yeu cau")  
