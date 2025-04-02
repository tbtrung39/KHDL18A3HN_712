import random
n = int(input("Nhap so phan tu: "))
a = [random.randint(1, n) for _ in range(n)]
print("Ta co danh sach: ", a)

#Phan tu lon thu 2 va vi tri cua phan tu do:
lon_nhat = max(a)
lon_2 = -1
for i in a:
    if i < lon_nhat and (lon_2 == -1 or i > lon_2):
        lon_2 = i
vt_lon_2 = -1
for x in range(len(a)):
    if a[x] == lon_2:
        vt_lon_2 = x
        
if lon_2 == -1:
    print("Khong co phan tu lon thu 2")
else:
    print("Phan tu lon thu 2 la: ", lon_2)
    print("Vi tri phan tu lon thu 2 la: ", vt_lon_2)

#So luong cac so duong lien tiep va tong lon nhat  
dai_max = 0
dem = 0
so = -1
tong_max = 0
dd_tong_max = 0
tong_ht = 0
dem_tong = 0
for i in a:
    if i > 0:
        if i == so + 1:
            dem += 1
        else:
            dem = 1
        so = i
        if dem > dai_max:
            dai_max = dem
    else:
        dem = 0
        so = -1
        
    if i > 0:
        tong_ht += i
        dem_tong += 1
        if tong_ht > tong_max:
            tong_max = tong_ht
            dd_tong_max = dem_tong
    else:
        tong_ht = 0
        dem = 0 
print("So luong cac so duong lien tiep nhieu nhat: ", dai_max)
print("So luong cac so duong lien tiep co tong lon nhat: ", dd_tong_max)
print("Tong lon nhat cua day so duong lien tiep: ", tong_max)