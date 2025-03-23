s1=input("nhập chuỗi 1: ")
s2=input("nhập chuỗi 2: ")
kq=""
i=0
while i<len(s1) or i<len(s2):
    if i<len(s1):
        kq+=s1[i]
    if i<len(s2):
        kq+=s2[i]
    i+=1
print("chuỗi trộn là:", kq)