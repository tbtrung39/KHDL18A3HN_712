ds=[]
while True:
    n=int(input("nhập số (nhập 0 để dừng): "))
    if n==0:
        break
    ds.append(n)
duong=[x for x in ds if x>0]
am=[x for x in ds if x<=0]
kq=duong+am
print("danh sách đa nhập: ", kq)
#chèn m
m=int(input("nhập số cần chèn: "))
vitri=int(input(f"nhập vị trí cần muốn chèn từ 0 đến {len(kq)}: "))
if 0<=vitri<=len(kq):
    kq.insert(vitri,m)
    print("danh sách sau khi chèn: ",kq)
else:
    print("vị trí không hơp lệ")