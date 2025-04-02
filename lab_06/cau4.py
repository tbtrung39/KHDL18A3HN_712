ds=[]
while True:
    n=int(input("nhap so danh sach (nhap 0 de dung) : "))
    if n==0:
        break
    ds.append(n)
#chèn
print("danh sach ban dau: ",ds)
ds=[1,2,3]+ds
ds.extend([1,2,3])
if len(ds)>=5:
    ds.insert(5,1)
    ds.insert(6,2)
    ds.insert(7,3)
    print("danh sach sau khi chen [1,2,3] vao vi tri thu 5 : ",ds)
else:
    print("danh sach khong du do dai de chen")
#xóa phần tử k
k=int(input("nhap vi tri k can xoa: "))
if 0<=k<=len(ds):
    del ds[k]
    print(f"danh sach sau khi xoa phan tu k {k}: {ds}")
else:
    print("vi tri khong hop le")
#sắp xếp
ds.sort()
print("danh sach sau khi xap xep tang dan: ",ds)
ds.sort(reverse=True)
print("danh sacch sau khi xap xep tang dan:", ds)