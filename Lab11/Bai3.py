def tim_cuc_tri(vao, ra):
    with open(vao, 'r', encoding='utf-8') as f_in:
        data = f_in.read()
    ds_so = list(map(int, data.strip().split()))
    cuc_tri = []
    for i in range(1, len(ds_so) - 1):
        if (ds_so[i] > ds_so[i-1] and ds_so[i] > ds_so[i+1]) or \
           (ds_so[i] < ds_so[i-1] and ds_so[i] < ds_so[i+1]):
            cuc_tri.append(ds_so[i])
    with open(ra, 'w', encoding='utf-8') as f_out:
        f_out.write(str(len(cuc_tri)) + '\n')
        f_out.write(' '.join(map(str, cuc_tri)))
tim_cuc_tri('f_in.dat', 'f_out.dat')