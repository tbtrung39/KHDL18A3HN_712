a=[1,2,3,2,4]
n=len(a)
ket_qua=[]
for i in range(n-1):
    for j in range(i+1,n):
        if a[i]<a[j]:
            ket_qua.append((i,j))
cap=ket_qua[-4:]
print("Các cặp số thỏa mãn:",cap)