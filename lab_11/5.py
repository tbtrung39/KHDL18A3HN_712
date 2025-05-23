sbd_pha = {}
with open(r"D:\24174600126_NguyenTienLuc_DHKL18A3\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\lab_11\Sbd_Pha.dat", "r") as f:
    for line in f:
        sbd, pha = line.strip().split()
        sbd_pha[sbd] = pha

sbd_ten = {}
with open(r"D:\24174600126_NguyenTienLuc_DHKL18A3\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\lab_11\Sbd_Ten.txt", "r") as f:
    for line in f:
        sbd, *name = line.strip().split()
        sbd_ten[sbd] = " ".join(name)

with open(r"D:\24174600126_NguyenTienLuc_DHKL18A3\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\KHDL18A3HN_712\lab_11\Phieu_Diem.txt", "r") as f:
    with open("Ketqua.txt", "w") as out:
        for line in f:
            pha, diem = line.strip().split()
            for sbd, p in sbd_pha.items():
                if p == pha:
                    out.write(f"{sbd} {sbd_ten[sbd]} {diem}\n")
