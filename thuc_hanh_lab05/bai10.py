s1=input("nhap chuoi 1: ")
s2=input("nhap chuoi 2: ")
max=""
for i in range(len(s1)):
    for j in range(i+1, len(s1)+1):
        kt=s1[i:j]
        if kt in s2 and len(kt)>len(max):
            max=kt
if max:
    print("chuoi con chung dai nhat la:", max)
else:
    print("khong co chuoi con chung")