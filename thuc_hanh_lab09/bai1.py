def tim_so_lon_nhat(ds):
    if len(ds)==1:
        return ds[0]
    else:
        lon_nhat_con_lai=tim_so_lon_nhat(ds[1:])
        if ds[0]>lon_nhat_con_lai:
            return ds[0]
        else:
            return lon_nhat_con_lai
a=float(input("nhap so thu nhat:"))
b=float(input("nhap so thu hai:"))
c=float(input("nhap so thu ba:"))
ds_so=[a,b,c]
kq=tim_so_lon_nhat(ds_so)
print("so lon nhat la:",kq)