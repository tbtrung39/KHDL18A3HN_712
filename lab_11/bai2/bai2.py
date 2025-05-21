with open(r'lab_11\bai_02\Inp.txt', 'r') as f: 
    dong = f.readline()  
cac_so = list(map(int, dong.split()))
cac_so.sort()
with open(r'lab_11\bai_02\out.txt', 'w') as tep_ra:
    tep_ra.write(' '.join(map(str, cac_so)))