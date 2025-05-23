with open(r"D:\24174600126_NguyenTienLuc_DHKL18A3\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\lab_11\Inp.txt", "r") as file:
    numbers = []
    for line in file:
        numbers.extend(map(int, line.strip().split()))
    numbers.sort()

with open("out.dat", "w") as f:
    f.write(" ".join(map(str, numbers)))