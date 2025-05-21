import os
# a) Ghép dữ liệu từ các tệp lại
def ghep_du_lieu(ten_folder):
    # Dùng đường dẫn tương đối
    sbd_ph_path = os.path.join(ten_folder, "Sbd_Ph.dat")
    sbd_ten_path = os.path.join(ten_folder, "SBD_Ten.txt")
    phieu_diem_path = os.path.join(ten_folder, "Phieu_Diem.txt")
# Đọc SBD -> Phách
    sbd_to_phach = {}
    with open(sbd_ph_path, 'r', encoding='utf-8') as f:
        for line in f:
            sbd, phach = map(int, line.strip().split())
            sbd_to_phach[sbd] = phach
# Đọc SBD -> Họ tên
    sbd_to_ten = {}
    with open(sbd_ten_path, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(maxsplit=1)
            sbd = int(parts[0])
            ho_ten = parts[1] if len(parts) > 1 else ""
            sbd_to_ten[sbd] = ho_ten
# Đọc Phách -> Điểm
    phach_to_diem = {}
    with open(phieu_diem_path, 'r', encoding='utf-8') as f:
        for line in f:
            phach, diem = line.strip().split()
            phach_to_diem[int(phach)] = float(diem)
   # (SBD, Họ tên, Điểm)
    ket_qua = []
    for sbd in sbd_to_phach:
        phach = sbd_to_phach[sbd]
        ten = sbd_to_ten.get(sbd, "Không rõ")
        diem = phach_to_diem.get(phach, 0.0)
        ket_qua.append((sbd, ten, diem))
    return ket_qua
# b) Ghi danh sách sắp xếp giảm dần ra file
def ghi_ket_qua(danh_sach, ten_folder):
    ketqua_path = os.path.join(ten_folder, "Ketqua.txt")
    danh_sach.sort(key=lambda x: -x[2])  
    with open(ketqua_path, 'w', encoding='utf-8') as f:
        for sbd, ten, diem in danh_sach:
            f.write(f"{sbd} {ten} {diem:.2f}\n")
folder = "baitap_bai5"
danh_sach = ghep_du_lieu(folder)
ghi_ket_qua(danh_sach, folder)
