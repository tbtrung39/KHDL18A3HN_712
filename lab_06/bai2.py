n=int(input("nhap so luong phan tu cua danh sach: "))
a=[]
print("nhap cac phan tu: ")
for i in range(n):
    a.append(int(input("-")))
if len(a)<2:
    print("khong du phan tu de tim so lon nhat")
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
    print(f"phan tu lon thu hai: {lon_thu_hai}, vi tri : {vi_tri_lon_thu_hai}")
#so luong cac so duong lien tiep
do_dai_max=0
do_dai_hien_tai=0
for i in a:
    if i>0:
        do_dai_hien_tai+=1
        if do_dai_hien_tai>do_dai_max:
            do_dai_max=do_dai_hien_tai
    else:
        do_dai_hien_tai=0
print(f"so luong cac so duong lien tiep nhieu nhat: {do_dai_max}")
#tong lon nhat
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
print(f"so luong cac so duong lien tiep ma tong lon nhat: {do_dai_max}")