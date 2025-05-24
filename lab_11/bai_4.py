import math
def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def uoc_nguyen_to(n):
    uoc = []
    for i in range(2, n + 1):
        if n % i == 0 and la_nguyen_to(i):
            uoc.append(i)
    return uoc

with open('KHDL18A3HN_712\lab_11\\f_in.dat', 'r') as tep_vao:
    cac_dong = tep_vao.readlines()
with open('f_out.dat', 'w') as tep_ra:
    for dong in cac_dong:
        so = int(dong.strip())
        uoc = uoc_nguyen_to(so)
        dong_ket_qua = ' '.join(map(str, uoc))
        tep_ra.write(dong_ket_qua + '\n')