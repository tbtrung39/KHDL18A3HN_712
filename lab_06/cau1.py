a=[2,-4,1,9,-3,6,3,-2,6,8]
tong=0
for so in a:
    tong+=so
print("tong cac phan tu: ", tong)
so_luong_ptu_duong=0
tong_ptu_duong=0
for so in a:
    if so>0:
        so_luong_ptu_duong+=1
        tong_ptu_duong+=so
print("so luong phan tu duong: ", so_luong_ptu_duong)
print("tong phan tu duong:", tong_ptu_duong)
vitri_ptu_am=1
for i, so in enumerate(a, start=1):
    if so<0:
        vitri_ptu_am=i-1
        break
print(vitri_ptu_am)
vitri_ptu_duong=1
for i in range(len(a)-1,-1,-1):
    if a[i]>0:
        vitri_ptu_duong=i
        break
print("vi tri phan tu duong cuoi cung:", vitri_ptu_duong)
phan_tu_lon_nhat=a[-1]
vitri_max_cuoi_cung=len(a)-1
for i in range(len(a)-2,-1,-1):
    if a[i]>phan_tu_lon_nhat:
        phan_tu_lon_nhat=a[i]
        vitri_max_cuoi_cung=i
print("phan tu lon nhat: ", phan_tu_lon_nhat)
print("vi tri phan tu ln nhat cuoi cung:", vitri_max_cuoi_cung)
