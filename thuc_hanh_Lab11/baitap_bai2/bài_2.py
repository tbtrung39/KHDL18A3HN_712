import os
def sap_xep_file(inp_file, out_file):
    with open(inp_file, 'r') as f:
        numbers = list(map(int, f.read().strip().split()))
    numbers.sort()
    with open(out_file, 'w') as f:
        f.write(' '.join(map(str, numbers)))

inp_path = os.path.join("baitap_bai2", "Inp.txt")
out_path = os.path.join("baitap_bai2", "out.dat")
sap_xep_file(inp_path, out_path)

