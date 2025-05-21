def tim_so_chung(file1='m_nums.txt', file2='n_nums.txt', output_file='so_chung.txt'):
    with open(file1, 'r') as f1:
        nums1 = set(map(int, f1.read().split()))

    with open(file2, 'r') as f2:
        nums2 = set(map(int, f2.read().split()))

    chung = sorted(nums1 & nums2)

    with open(output_file, 'w') as out:
        out.write(' '.join(map(str, chung)))

    print("Các số chung:")
    print(' '.join(map(str, chung)))
