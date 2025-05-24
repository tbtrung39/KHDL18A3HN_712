with open("dayso.dat", "r") as f:
    du_lieu = f.read()  
cac_so = map(int, du_lieu.split())
tong_le = sum(so for so in cac_so if so % 2 != 0)
print("tong cac so le trong day la", tong_le)