def ghep_phach():
    sbd_phach = {}
    with open('Sbd_Ph.dat', 'r') as f1:
        for line in f1:
            parts = line.strip().split()
            if len(parts) == 2:
                sbd, phach = parts
                sbd_phach[phach] = sbd

    sbd_ten = {}
    with open('Sbd_Ten.txt', 'r') as f2:
        for line in f2:
            parts = line.strip().split(maxsplit=1)
            if len(parts) == 2:
                sbd, ten = parts
                sbd_ten[sbd] = ten

    phach_diem = {}
    with open('Phieu_Diem.txt', 'r') as f3:
        for line in f3:
            parts = line.strip().split()
            if len(parts) == 2:
                phach, diem = parts
                phach_diem[phach] = float(diem)

    ketqua = []
    for phach, sbd in sbd_phach.items():
        ten = sbd_ten.get(sbd, "Không rõ")
        diem = phach_diem.get(phach, 0)
        ketqua.append((sbd, ten, diem))

    ketqua.sort(key=lambda x: x[2], reverse=True)

    with open('Ketqua.txt', 'w') as f_out:
        for sbd, ten, diem in ketqua:
            f_out.write(f"{sbd} {ten} {diem:.2f}\n")

    print("Đã ghi file Ketqua.txt.")


ghep_phach()
