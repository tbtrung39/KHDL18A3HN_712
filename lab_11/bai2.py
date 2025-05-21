with open('Inp.txt', 'r') as tep_vao: 
    dong = tep_vao.readline()  
cac_so = list(map(int, dong.split()))
cac_so.sort()
with open('out.dat', 'w') as tep_ra:
    tep_ra.write(' '.join(map(str, cac_so)))
