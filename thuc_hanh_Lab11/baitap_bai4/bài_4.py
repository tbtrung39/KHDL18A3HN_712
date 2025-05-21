import os
import math
def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def uoc_so_nguyen_to(n):
    uoc = []
    for i in range(2, n + 1):
        if n % i == 0 and la_nguyen_to(i):
            uoc.append(i)
    return uoc
def xu_ly_file(input_file, output_file):
    with open(input_file, 'r') as f:
        so_list = [int(line.strip()) for line in f.readlines()]
    with open(output_file, 'w') as f:
        for so in so_list:
            uoc = uoc_so_nguyen_to(so)
            f.write(' '.join(map(str, uoc)) + '\n')
inp_path = os.path.join("baitap_bai4", "f_in.dat")
out_path = os.path.join("baitap_bai4", "f_out.dat")

xu_ly_file(inp_path, out_path)
