with open(r"D:\24174600126_NguyenTienLuc_DHKL18A3\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\lab_11\passengers.in") as f:
    n = int(f.readline())
    weights = []

    for _ in range(n):
        f.readline()
        items = list(map(float, f.readline().split()))
        weights.append(sum(items))

with open("WEIGHT.OUT", "w") as f:
    for w in weights:
        f.write(f"{w:.2f}\n")

with open("CANCELED.OUT", "w") as f:
    for i, w in enumerate(weights, 1):
        if w > 23:
            f.write(f"{i}\n")
