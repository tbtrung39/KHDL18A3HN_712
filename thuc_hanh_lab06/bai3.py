ds=[]
while True:
    n=int(input("nhap so (nhap 0 de dung) la: "))
    if n==0:
        break
    ds.append(n)
duong=[x for x in ds if x>0]
am=[x for x in ds if x<=0]
kq=duong+am
print("danh sach da nhap: ", kq)
#chèn m
m=int(input("nhap so can chen la: "))
vi_tri=int(input(f"nhap vi tri can muon chen tu 0 den {len(kq)} la: "))
if 0<=vi_tri<=len(kq):
    kq.insert(vi_tri,m)
    print("danh sach sau khi chen la: ",kq)
else:
    print("vi tri khong hop le ")