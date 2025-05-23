with open("m_nums.txt", 'r') as f:
    ds_so_m = set(int(x) for x in f.read().split())

with open("n_num.txt", 'r') as f:
    ds_so_n = set(int(x) for x in f.read().split())

so_chung = ds_so_m.intersection(ds_so_n)

with open("so_chung.txt", 'w') as f:
    f.write(' '.join(map(str, so_chung)))