a = [2,-4,1,9,-3,6,3,-2,6,8]

tong = 0
for i in a:
    tong += i
print("Tong cua day la: ",tong)

dem = 0
tong_duong = 0
for j in a:
    if i > 0:
        dem += 1
        tong_duong += j
print("So luong cac so duong la: ", dem)
print("Tong cac so duong la: ", tong_duong)
    
vt = -1
for x in range(len(a)):
    if a[x] < 0:
        vt = x
        break
print("Vi tri phan tu am dau tien la: ", vt)
       
       
vt = -1
for y in range(len(a)):
    if a[y] > 0:
        vt = y
print("Vi tri cua phan tu duong cuoi cung la: ", vt)

lon_nhat = 0
vt_lon_nhat = 0
for e in range(len(a)):
    if a[e] > lon_nhat:
        lon_nhat = a[e]
        vt_lon_nhat = e
print("Phan tu lon nhat la: ", lon_nhat)
print("Vi tri phan tu lon nhat cuoi cung la: ", vt_lon_nhat)
