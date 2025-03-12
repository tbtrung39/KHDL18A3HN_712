n=input("nhập số: ")
tap_so=["không","một","hai","ba","bốn","năm","sáu","bảy","tám","chín"]
i=0
kq=""
while i<len(n):
    chu=int(n[i])
    kq+=tap_so[chu]+""
    i+=1
print(kq)