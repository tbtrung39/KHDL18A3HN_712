a=[2,-4,1,9,-3,6,3,-2,6,8]
tong=0
for so in a:
    tong+=so
print("tong cac phan tu la: ", tong)
so_luong_phan_tu_duong=0
tong_phan_tu_duong=0
for so in a:
    if so>0:
        so_luong_phan_tu_duong+=1
        tong_phan_tu_duong+=so
print("so luong phan tu duong la: ", so_luong_phan_tu_duong)
print("tong phan tu duong la:", tong_phan_tu_duong)
vi_tri_phan_tu_am=1
for i, so in enumerate(a, start=1):
    if so<0:
        vi_tri_phan_tu_am=i-1
        break
print(vi_tri_phan_tu_am)
vi_tri_phan_tu_duong=1
for i in range(len(a)-1,-1,-1):
    if a[i]>0:
        vi_tri_phan_tu_duong=i
        break
print("vi tri phan tu duong cuoi cung la:", vi_tri_phan_tu_duong)
phan_tu_lon_nhat=a[-1]
vi_tri_max_cuoi_cung=len(a)-1
for i in range(len(a)-2,-1,-1):
    if a[i]>phan_tu_lon_nhat:
        phan_tu_lon_nhat=a[i]
        vi_tri_max_cuoi_cung=i
print("phan tu lon nhat la: ", phan_tu_lon_nhat)
print("vi tri phan tu ln nhat cuoi cung la:", vi_tri_max_cuoi_cung)