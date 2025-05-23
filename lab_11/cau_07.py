def tim_so_chung():
    file_m = 'm_nums.txt'
    file_n = 'n_nums.txt'
    file_kq = 'so_chung.txt'

    with open(file_m, 'r', encoding='utf-8') as f_m:
        so_m = set()
        for line in f_m.readlines():
            so_m.update(map(int, line.strip().split()))

    with open(file_n, 'r', encoding='utf-8') as f_n:
        so_n = set()
        for line in f_n.readlines():
            so_n.update(map(int, line.strip().split()))

    so_chung = []
    for num in so_m:
        if num in so_n:
            so_chung.append(num)
    so_chung.sort()

    with open(file_kq, 'w', encoding='utf-8') as f_out:
        for num in so_chung:
            f_out.write(str(num) + '\n')

    print("Các số chung trong cả 2 file:")
    with open(file_kq, 'r', encoding='utf-8') as f_out:
        print(f_out.read())

tim_so_chung()
