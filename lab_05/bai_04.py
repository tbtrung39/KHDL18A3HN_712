Str1 = input("Nhap chuoi 1: ")
Str2 = input("Nhap chuoi 2: ")
cong = Str1 + Str2
print(cong)

Str1 = "345"
Str2 = "4567"
kq = ""
do_dai = len(Str1)
if len(Str2) > do_dai:
    do_dai = len(Str2)
    
for i in range(do_dai):
    if i < len(Str1):
        kq += Str1[i]
    if i < len(Str2):
        kq += Str2[i]
        
print("Ket qua tron chuoi 1 va 2: ", kq)  