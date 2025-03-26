n=input("nhap chuoi ky tu: ")
s=0
for i in n:
    if i.isdigit() or i.isalpha():
        s+=0
    else:
        s+=1
print(f"so ky tu khong phai la chu hoac so la: {s}")