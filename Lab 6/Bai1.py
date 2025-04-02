#Bai1
a=[2,-4,1,9,-3,6,3,-2,6,8]
#a.Tính tổng các phần tử của danh sách
tong=sum(a)
print("Tổng các phần tử:",tong)
#b.Đếm số lượng các số hạng dương và tổng của các số hạng dương
so_duong=[]
for i in range(len(a)):
    if a[i]>0:
        so_duong.append(a[i])
so_luong_duong=len(so_duong)
tong_duong=sum(so_duong)
print("Số lượng số dương:",so_luong_duong)
print("Tổng các số dương:",tong_duong)
#c.Vị trí của phần tử âm đầu tiên trong danh sách
vi_tri_am_dau=[]
for i in range(len(a)):
    if a[i]<0:
        vi_tri_am_dau=i
        break
print("Vị trí phần tử âm đầu tiên:",vi_tri_am_dau)
#d.Vị trí của phần tử dương cuối cùng trong danh sách
vi_tri_duong_cuoi=[]
for i in range(len(a)-1,-1,-1):
    if a[i]>0:
        vi_tri_duong_cuoi=i
        break
print("Vị trí phần tư dương cuối cùng:",vi_tri_duong_cuoi)
#e.Phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng
pt_lon_nhat=a[0]
for i in range(1,len(a)):
    if a[i]>pt_lon_nhat:
        pt_lon_nhat=a[i]
vi_tri_cuoi_max=[]
for i in range(len(a)-1,-1,-1):
    if a[i]==pt_lon_nhat:
        vi_tri_cuoi_max=i
        break
print("Phần tử lớn nhất:",pt_lon_nhat)
print("Vị trí phần tử lớn nhất cuối cùng:",vi_tri_cuoi_max)