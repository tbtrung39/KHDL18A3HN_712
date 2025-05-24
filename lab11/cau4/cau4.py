import math
def nt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def uoc_nguyen_to(n):
    uoc = []
    for i in range(2, n + 1):
        if n % i == 0 and nt(i):
            uoc.append(i)
    return uoc

with open(r'cau4\f_in.dat', 'r') as f:
    cac_dong = f.readlines()
with open(r'cau4\f_out.dat', 'w') as s:
    for dong in cac_dong:
        so = int(dong.strip())
        uoc = uoc_nguyen_to(so)
        dong_ket_qua = ' '.join(map(str, uoc))
        s.write(dong_ket_qua + '\n')