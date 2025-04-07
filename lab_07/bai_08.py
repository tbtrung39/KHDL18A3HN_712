A = [34, 22, 63, "T1", "Max", "Uneti", -10]
sn = 0
st = 0
ckt = 0
for i in A:
    if isinstance(i,int):
        sn+=1
    elif isinstance(i,float):
        st+=1
    elif isinstance(i,str):
        ckt+=1
print("So nguyen: ",sn)
print("So thuc: ",st)
print("Chuoi ky tu: ",ckt)