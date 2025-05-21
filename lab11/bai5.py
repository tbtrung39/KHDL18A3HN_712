def ghep_phach():
    with open('Sbd_Ph.dat', 'r') as f:
        sbd_ph = {int(a): int(b) for a, b in (line.split() for line in f)}

    with open('Sbd_Ten.txt', 'r') as f:
        sbd_ten = {int(line.split()[0]): ' '.join(line.split()[1:]) for line in f}

    with open('Phieu_Diem.txt', 'r') as f:
        phach_diem = {int(a): int(b) for a, b in (line.split() for line in f)}

    ds_thi_sinh = []
    for sbd, phach in sbd_ph.items():
        if sbd in sbd_ten and phach in phach_diem:
            ho_ten = sbd_ten[sbd]
            diem = phach_diem[phach]
            ds_thi_sinh.append((sbd, ho_ten, diem))

    ds_thi_sinh.sort(key=lambda x: -x[2])  # giảm dần theo điểm

    with open('Ketqua.txt', 'w') as f:
        for sbd, ho_ten, diem in ds_thi_sinh:
            f.write(f"{sbd} {ho_ten} {diem}\n")
