with open('f_in.dat', 'r') as tep_vao: 
    dong = tep_vao.readline()
day_so = list(map(int, dong.split()))
cuc_tri = []
for i in range(1, len(day_so) - 1):
    if (day_so[i] > day_so[i - 1] and day_so[i] > day_so[i + 1]) or \
       (day_so[i] < day_so[i - 1] and day_so[i] < day_so[i + 1]):
        cuc_tri.append(day_so[i])

# ghi kq
with open('f_out.dat', 'w') as tep_ra:
    tep_ra.write(str(len(cuc_tri)) + '\n')  
    tep_ra.write(' '.join(map(str, cuc_tri)))  