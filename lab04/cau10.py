n=input("nhập số: ")
tap_so=["không","một","hai","ba","bốn","năm","sáu","bảy","tám","chín"]
i=0
kq=""
while i<len(n):
    if n[i]==".":
        kq+="phẩy"
    elif n[i]=="-":
        kq+="âm"
    else:
        chu=int(n[i])
        kq+=tap_so[chu]+""
    i+=1
print(kq.strip(" "))