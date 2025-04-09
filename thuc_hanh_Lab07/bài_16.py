day_so=[1,2,3,2,4]
tu_dien={}
for vi_tri in range(len(day_so)):
    so=day_so[vi_tri]
    if so not in tu_dien:
        tu_dien[so]=[]
    tu_dien[so].append(vi_tri)
tap_ket_qua=set()
for i in range(len(day_so)):
    so_can_tim=day_so[i]+1
    if so_can_tim in tu_dien:
        for j in tu_dien:
            if i<j:
                tap_ket_qua.add((i,j))
print(sorted(tap_ket_qua))