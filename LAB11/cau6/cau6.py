duong_dan=input("Nhap ten tep de doc/ghi:")
with open(duong_dan)as f:
    dong=f.read().splitlines()

print(dong[0])
print("— đây là ý a, phần 1: in dòng đầu tiên của file.\n")

print(dong[2])
print("— đây là ý a, phần 2: in dòng thứ ba của file.\n")

print("\n".join(dong))
print("— đây là ý b: in toàn bộ nội dung file.\n")

ma_tran=[]
for d in dong:
    ds=list(map(int,d.split()))
    while len(ds)<4:ds.append(0)
    ma_tran.append([x if x%2 else 0 for x in ds])
while len(ma_tran)<4:ma_tran.append([0]*4)

with open("ODD.txt","w")as f:
    for d in ma_tran:f.write(" ".join(map(str,d))+"\n")

print(" ".join(map(str,ma_tran[-1])))
print("— đây là ý d: in dòng cuối cùng của file ODD.txt")
