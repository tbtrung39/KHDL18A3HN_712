with open(r"cau2\int.txt","r") as f:
    dong=f.readline()
cac_so=list(map(int,dong.split()))
cac_so.sort()
with open(r"cau2\out.txt","w") as e:
    e.write(' '.join(map(str,cac_so))) 