ds=[]
while True:
    n=int(input("nhập số vào danh sách hoặc 0 để dừng: "))
    if n==0:
        break
    ds.append(n)
#chèn
print("danh sách ban đầu: ",ds)
ds=[1,2,3]+ds
ds.extend([1,2,3])
if len(ds)>=5:
    ds.insert(5,1)
    ds.insert(6,2)
    ds.insert(7,3)
    print("danh sách sau khi chèn [1,2,3] vào vị tri thứ 5: ",ds)
else:
    print("danh sách khong đủ độ dài để chèn")
#xóa phần tử k
k=int(input("nhập vị trí k cần xóa: "))
if 0<=k<=len(ds):
    del ds[k]
    print(f"danh sách sau khi xóa phần tử {k}: {ds}")
else:
    print("vị trí không hợp lệ")
#sắp xếp
ds.sort()
print("danh sách sau khi sắp xếp tăng dần: ",ds)
ds.sort(reverse=True)
print("danh sách sau khi sắp xêps giảm dần:", ds)