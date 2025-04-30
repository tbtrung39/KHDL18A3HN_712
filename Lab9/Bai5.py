#Bai5
def permutation(n):
    if n==1:
        return[[1]]
    else:
        kq=[]
        cac_hoan_vi_truoc=permutation(n-1)
        for hoan_vi in cac_hoan_vi_truoc:
            for i in range(len(hoan_vi)+1):
                hoan_vi_moi=hoan_vi[:i]+[n]+hoan_vi[i:]
                kq.append(hoan_vi_moi)
        return kq
n=int(input("Nhập số n:"))
kq=permutation(n)
print("Các hoán vị của dãy từ 1 đến", n,"là:")
for dong in kq:
    print(dong)