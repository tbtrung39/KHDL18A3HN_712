van_ban=input("nhập đoạn văn: ")
tu_can_tim=input("nhập từ đơn: ")
for dau in ",.::!?-()\"'":
    van_ban=van_ban.replace(dau, " ")
van_ban=van_ban.lower()
tu_can_tim=tu_can_tim.lower()
ds_tu=van_ban.split()
dem=0
for tu in ds_tu:
    if tu==tu_can_tim:
        dem+=1
print(f"từ '{tu_can_tim}' xuất hiện {dem} lần.")

#cách 2
vb=input("nhập đoạn văn: ")
td=input("Nhập từ đơn: ")
for k in ",.::!?-()\"'":
    vb=vb.replace(k, " ")
ds=vb.lower().split()
td=td.lower()
dem=ds.count(td)
print(f"Từ '{td}' xuất hiện {dem} lần.")