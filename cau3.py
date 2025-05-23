def tim_cuc_tri(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        line = file.readline()
        ds_so = [int(x) for x in line.strip().split()]

    cuc_tri = []
    n = len(ds_so)

    for k in range(1, n-1):
        if (ds_so[k-1] < ds_so[k] > ds_so[k+1]) or (ds_so[k-1] > ds_so[k] < ds_so[k+1]):
            cuc_tri.append(ds_so[k])

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(str(len(cuc_tri)) + '\n')
        file.write(' '.join(str(x) for x in cuc_tri))

tim_cuc_tri('f_in.dat', 'f_out.dat')
