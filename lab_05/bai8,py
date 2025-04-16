van_ban=input("nhap doan van: ")
tu_can_tim=input("nhap tu don: ")
for dau in ",.::!?-()\"'":
    van_ban=van_ban.replace(dau, " ")
van_ban=van_ban.lower()
tu_can_tim=tu_can_tim.lower()
ds_tu=van_ban.split()
dem=0
for tu in ds_tu:
    if tu==tu_can_tim:
        dem+=1
print(f"tu '{tu_can_tim}' xuat hien {dem} lan.")

#cách 2
vb=input("nhap doan van: ")
td=input("nhap tu don: ")
for k in ",.::!?-()\"'":
    vb=vb.replace(k, " ")
ds=vb.lower().split()
td=td.lower()
dem=ds.count(td)
print(f"tu '{td}' xuat hien {dem} lan.")