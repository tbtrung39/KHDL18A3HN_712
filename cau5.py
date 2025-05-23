def ghep_phach():
    file_sbd_phach = 'Sbd_Ph.dat'
    file_sbd_ten = 'Sbd_Ten.txt'
    file_phieu_diem = 'Phieu_Diem.txt'
    file_ketqua = 'Ketqua.txt'
    sbd_phach = {}
    with open(file_sbd_phach, 'r', encoding='utf-8') as f1:
        for line in f1:
            sbd, phach = map(int, line.strip().split())
            sbd_phach[phach] = sbd
    sbd_ten = {}
    with open(file_sbd_ten, 'r', encoding='utf-8') as f2:
        for line in f2:
            line = line.strip()
            vi_tri_cach = line.find(' ')
            sbd = int(line[:vi_tri_cach])
            ho_ten = line[vi_tri_cach+1:]
            sbd_ten[sbd] = ho_ten
    ds_thi_sinh = []
    with open(file_phieu_diem, 'r', encoding='utf-8') as f3:
        for line in f3:
            phach_str, diem_str = line.strip().split()
            phach = int(phach_str)
            diem = float(diem_str)
            if phach in sbd_phach:
                sbd = sbd_phach[phach]
                ten = sbd_ten.get(sbd, "Chưa rõ")
                ds_thi_sinh.append((sbd, ten, diem))
    ds_thi_sinh.sort(key=lambda x: x[2], reverse=True)

    with open(file_ketqua, 'w', encoding='utf-8') as f_out:
        for sbd, ten, diem in ds_thi_sinh:
            f_out.write(f"{sbd} {ten} {diem:.2f}\n")
ghep_phach()
