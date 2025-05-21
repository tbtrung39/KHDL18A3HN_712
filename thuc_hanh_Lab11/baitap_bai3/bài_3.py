import os
def tim_cuc_tri(input_file, output_file):
    with open(input_file, 'r') as f:
        day_so = list(map(int, f.read().strip().split()))
    cuc_tri = []
    for i in range(1, len(day_so) - 1):
        if (day_so[i] > day_so[i - 1] and day_so[i] > day_so[i + 1]) or \
           (day_so[i] < day_so[i - 1] and day_so[i] < day_so[i + 1]):
            cuc_tri.append(day_so[i])
    with open(output_file, 'w') as f:
        f.write(str(len(cuc_tri)) + '\n')            
        f.write(' '.join(map(str, cuc_tri)))         
inp_path = os.path.join("baitap_bai3", "f_in.dat")
out_path = os.path.join("baitap_bai3", "f_out.dat")
tim_cuc_tri(inp_path, out_path)
