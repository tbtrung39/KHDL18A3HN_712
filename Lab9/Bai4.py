#Bai4
def hoan_vi(ds, vtri):
    if vtri == len(ds):
        print(ds)
        return
    else:
        for i in range(vtri, len(ds)):
            ds[vtri], ds[i] = ds[i], ds[vtri]
            hoan_vi(ds, vtri + 1)
            ds[vtri], ds[i] = ds[i], ds[vtri]
n = int(input("Nhập số tự nhiên n: "))
ds= list(range(1, n + 1))
hoan_vi(ds, 0)