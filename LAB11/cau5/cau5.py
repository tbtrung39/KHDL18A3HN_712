d1=input("Nhap duong dan tep Sbd_Ph.dat:")
d2=input("Nhap duong dan tep SBD_Ten.txt:")
d3=input("Nhap duong dan tep Phieu_Diem.txt:")
with open(d1)as f:sdph={int(l.split()[0]):int(l.split()[1])for l in f}
with open(d2,encoding="utf-8")as f:sdten={int(l.split()[0]):" ".join(l.split()[1:])for l in f}
with open(d3)as f:phdiem={int(l.split()[0]):float(l.split()[1])for l in f}
ds=[(sbd,sdten.get(sbd,""),phdiem.get(soph,0))for sbd,soph in sdph.items()]
ds.sort(key=lambda x:x[2],reverse=True)
with open("Ketqua.txt","w",encoding="utf-8")as f:
    for sbd,ten,diem in ds:f.write(f"{sbd} {ten} {diem}\n")
print("Da ghi ket qua vao tep Ketqua.txt")
