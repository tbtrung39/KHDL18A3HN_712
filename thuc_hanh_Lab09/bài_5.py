def permutation(n):
    if n==1:
        return[[1]]
    else:
        hoan_vi_n_1=permutation(n-1)
        ket_qua=[]
        for hv in hoan_vi_n_1:
            for i in range(len(hv)+1):
                moi=hv[:i]+[n]+hv[i:]
                ket_qua.append(moi)
        return ket_qua
n=int(input("Nhập số nguyênduwong n:"))
ds_hoan_vi=permutation(n)
print(f"Tất cả các hoán vị{n}(tổng cộng{len(ds_hoan_vi)}):")
for hv in ds_hoan_vi:
    print(hv)
    