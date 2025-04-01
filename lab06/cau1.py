a=[2,-4,1,9,-3,6,3,-2,6,8]
#tong cac phan tu
tong=0
for so in a:
    tong+=so
print("Tổng các phần tử: ", tong)
#số lượng và tổng các số dương
so_luong_ptu_duong=0
tong_ptu_duong=0
for so in a:
    if so>0:
        so_luong_ptu_duong+=1
        tong_ptu_duong+=so
print("Số lượng phần tử dương: ", so_luong_ptu_duong)
print("tổng phần tử dương:", tong_ptu_duong)
#vị trí phần tử âm đầu tiên
vitri_ptu_am=1
for i, so in enumerate(a, start=1):
    if so<0:
        vitri_ptu_am=i-1
        break
print(vitri_ptu_am)
#vị trí phần tư dương cuối cùng
vitri_ptu_duong=1
for i in range(len(a)-1,-1,-1):
    if a[i]>0:
        vitri_ptu_duong=i
        break
print("vị trí phần tử dương cuối cùng:", vitri_ptu_duong)
#tìm phần tử lớn nhất và vị trí cuối cùng của nó
phan_tu_lon_nhat=a[-1]
vitri_max_cuoi_cung=len(a)-1
for i in range(len(a)-2,-1,-1):
    if a[i]>phan_tu_lon_nhat:
        phan_tu_lon_nhat=a[i]
        vitri_max_cuoi_cung=i
print("phan tu lớn nhất: ", phan_tu_lon_nhat)
print("vị trí phần tử lớn nhất cuôi cùng:", vitri_max_cuoi_cung)
