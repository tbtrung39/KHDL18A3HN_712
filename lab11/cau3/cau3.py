with open(r'cau3\f_in.dat', 'r') as f: 
    dong = f.readline()
day_so = list(map(int, dong.split()))
cuc_tri = []
for i in range(1, len(day_so) - 1):
    if (day_so[i] > day_so[i - 1] and day_so[i] > day_so[i + 1]) or \
       (day_so[i] < day_so[i - 1] and day_so[i] < day_so[i + 1]):
        cuc_tri.append(day_so[i])


with open(r'cau3\f_out.dat', 'w') as s:
    s.write(str(len(cuc_tri)) + '\n')  
    s.write(' '.join(map(str, cuc_tri)))  