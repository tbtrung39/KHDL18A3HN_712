with open('Sbd_Ph.dat') as file1, open('SBD_Ten.txt') as file2,open('Phieu_Diem.txt') as file3:
    sbd_ph = [tuple(map(int, line.strip().split())) for line in file1]
    sbd_ten = dict(map(lambda x: (int(x[0]), x[1]),[line.strip().split(maxsplit=1) for line in file2]))
    phieu_diem = dict(map(lambda x: (int(x[0]), float(x[1])),[line.strip().split() for line in file3]))
thong_tin = []
for sbd, so_phach in sbd_ph:
    if sbd in sbd_ten and so_phach in phieu_diem:
        ten = sbd_ten[sbd]
        diem = phieu_diem[so_phach]
        thong_tin.append((sbd, ten, diem))
thong_tin.sort(key=lambda x: x[2], reverse=True)
with open('Ketqua.txt', 'w', encoding='utf-8') as file:
    for sbd, ten, diem in thong_tin:
        file.write(f'{sbd} {ten} {diem}\n')