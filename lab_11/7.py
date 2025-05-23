with open(r"D:\24174600126_NguyenTienLuc_DHKL18A3\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\lab_11\m_nums.txt") as f1, open(r"D:\24174600126_NguyenTienLuc_DHKL18A3\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\lab_11\n_nums.txt") as f2:
    m = set(map(int, f1.read().split()))
    n = set(map(int, f2.read().split()))

    common = m & n
    with open("so_chung.txt", "w") as f:
        f.write(" ".join(map(str, sorted(common))))
