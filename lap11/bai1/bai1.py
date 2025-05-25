with open(r"cau1\dayso.dat","r") as file:
    doc=file.read()
cac_so=map(int,doc.split())
tong_le=sum(so for so in cac_so if so%2!=0)
print("tong cac do le la: ",tong_le)