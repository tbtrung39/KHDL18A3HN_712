with open(r'lab_11\bai_05\sbd_ph.dat', 'r') as f: 
    sbd_phach = {}
    for dong in f:
        sbd, phach = map(int, dong.strip().split())
        sbd_phach[sbd] = phach

with open(r'lab_11\bai_05\sbd_ten.txt', 'r') as f:
    sbd_ten = {}
    for dong in f:
        parts = dong.strip().split()
        sbd = int(parts[0])
        ten = ' '.join(parts[1:])  
        sbd_ten[sbd] = ten

with open(r'lab_11\bai_05\phieu_diem.txt', 'r') as f:
    phach_diem = {}
    for dong in f:
        phach, diem = map(float, dong.strip().split())
        phach_diem[int(phach)] = diem

danh_sach_thisinh = []
for sbd in sbd_phach:
    phach = sbd_phach[sbd]
    ten = sbd_ten.get(sbd, "Không rõ")
    diem = phach_diem.get(phach, 0)
    danh_sach_thisinh.append((sbd, ten, diem))

danh_sach_thisinh.sort(key=lambda x: x[2], reverse=True)

with open(r'lab_11\bai_05\ket_qua.txt', 'w') as f:
    for sbd, ten, diem in danh_sach_thisinh:
        f.write(f"{sbd} {ten} {diem}\n")