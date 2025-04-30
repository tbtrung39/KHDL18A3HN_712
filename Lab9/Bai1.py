#Bai1
def so_lon_nhat(ds):
    if len(ds)==1:
        return ds[0]
    else:
        lon_nhat_con_lai=so_lon_nhat(ds[1:])
        if ds[0]>lon_nhat_con_lai:
            return ds[0]
        else:
            return lon_nhat_con_lai
a=float(input("Nhập số thứ nhất:"))
b=float(input("Nhập số thứ hai:"))
c=float(input("Nhập số thứ ba:"))
ds_so=[a,b,c]
kq=so_lon_nhat(ds_so)
print("Số lớn nhất là:",kq)