n=int(input("nhập số lượng phần tư của danh sách: "))
a=[]
print("nhập các phàn tử: ")
for i in range(n):
    a.append(int(input("-")))
if len(a)<2:
    print("không đủ phần tử để tìm số lớn nhất")
else:
    lon_nhat=lon_thu_hai=a[0]
    vi_tri_lon_thu_hai=1
    vi_tri_lon_thu_nhat=0
    for i in range(1,len(a)):
        if a[i]>lon_nhat:
            lon_thu_hai=lon_nhat
            vi_tri_lon_thu_hai=vi_tri_lon_thu_nhat
            lon_nhat=a[i]
            vi_tri_lon_thu_nhat=i
        elif a[i]>lon_thu_hai and a[i]!=lon_nhat:
            lon_thu_hai=a[i]
            vi_tri_lon_thu_hai=i
    print(f"phần tử lớn thứ hai: {lon_thu_hai}, vị trí: {vi_tri_lon_thu_hai}")
#số lượng các số dương liên tiếp
do_dai_max=0
do_dai_hien_tai=0
for i in a:
    if i>0:
        do_dai_hien_tai+=1
        if do_dai_hien_tai>do_dai_max:
            do_dai_max=do_dai_hien_tai
    else:
        do_dai_hien_tai=0
print(f"số lượng các số dương liên tiếp nhiều nhất: {do_dai_max}")
#số lượng các số dương liên tiếp có tổng lớn nhất
tong_max=0
tong_hien_tai=0
do_dai_max=0
do_dai_hien_tai=0
for i in a:
    if i>0:
        tong_hien_tai+=i
        do_dai_hien_tai+=1
        if tong_hien_tai>tong_max:
            tong_hien_tai=tong_max
            do_dai_max=do_dai_hien_tai
    else:
        tong_hien_tai=0
        do_dai_hien_tai=0
print(f"sô lượng các số dương liên tiếp mà tổng lớn nhất: {do_dai_max}")

