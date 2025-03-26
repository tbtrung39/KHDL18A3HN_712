#Bai4
s1 = input("Nhập chuỗi S1: ")
s2 = input("Nhập chuỗi S2: ")
for i in range(max(len(s1), len(s2))):
    if i<len(s1):
        print(s1[i], end='')
    if i<len(s2):
        print(s2[i], end='')