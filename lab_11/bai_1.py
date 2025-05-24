with open('KHDL18A3HN_712\lab_11\dayso.dat', 'r') as tep:
    du_lieu = tep.read()  
cac_so = map(int, du_lieu.split())
tong_le = sum(so for so in cac_so if so % 2 != 0)
print("Tong cac so le trong day la: ", tong_le)