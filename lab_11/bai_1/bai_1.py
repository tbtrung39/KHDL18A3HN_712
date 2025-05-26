with open(r'lab_11\bai_01\dayso.dat', 'r') as f:
    doc = f.read()
cac_so = map(int, doc.split())
tong_le = sum(so for so in cac_so if so % 2 != 0)
print("Tong cac so le la: ",tong_le)