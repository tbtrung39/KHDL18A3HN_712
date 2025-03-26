#Cách 1:
van_ban=input("Nhap doan van: ")
tu_can_tim=input("Nhap tu can tim: ")
for dau in ",.::!?-()\"'":
    van_ban=van_ban.replace(dau, " ")
van_ban=van_ban.lower()
tu_can_tim=tu_can_tim.lower()
ds_tu=van_ban.split()
dem=0
for tu in ds_tu:
    if tu==tu_can_tim:
        dem+=1
print(f"Tu '{tu_can_tim}' xuat hien {dem} lan.")

#Cách 2:
vb=input("Nhap doan van: ")
td=input("Nhap tu can tim: ")
for k in ",.::!?-()\"'":
    vb=vb.replace(k, " ")
ds=vb.lower().split()
td=td.lower()
dem=ds.count(td)
print(f"Tu '{td}' xuat hien {dem} lan.")