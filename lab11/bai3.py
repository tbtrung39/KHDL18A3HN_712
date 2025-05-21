def tim_cuc_tri(input_file='f_in.dat', output_file='f_out.dat'):
    with open(input_file, 'r') as f:
        a = list(map(int, f.readline().strip().split()))
    cuc_tri = []
    for i in range(1, len(a) - 1):
        if (a[i] > a[i-1] and a[i] > a[i+1]) or (a[i] < a[i-1] and a[i] < a[i+1]):
            cuc_tri.append(a[i])
    with open(output_file, 'w') as f:
        f.write(f"{len(cuc_tri)}\n")
        f.write(' '.join(map(str, cuc_tri)))
