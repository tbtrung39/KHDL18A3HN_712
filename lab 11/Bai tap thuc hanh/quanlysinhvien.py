
import csv

class SinhVien:
    def __init__(self, ma_sv, ho_ten, diem_tb, diem_rl):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.diem_tb = float(diem_tb)
        self.diem_rl = float(diem_rl)
        self.diem_tl = (self.diem_tb + self.diem_rl) / 2

    def to_list(self):
        return [self.ma_sv, self.ho_ten, self.diem_tb, self.diem_rl, self.diem_tl]

def nhap_danh_sach_sv():
    danh_sach = []
    n = int(input("Nhập số lượng sinh viên: "))
    for _ in range(n):
        ma_sv = input("Mã SV: ")
        ho_ten = input("Họ tên: ")
        diem_tb = input("Điểm TB: ")
        diem_rl = input("Điểm RL: ")
        danh_sach.append(SinhVien(ma_sv, ho_ten, diem_tb, diem_rl))
    return danh_sach

def luu_file_csv(danh_sach, file_path):
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Mã SV", "Họ tên", "Điểm TB", "Điểm RL", "Điểm TL"])
        for sv in danh_sach:
            writer.writerow(sv.to_list())

def sap_xep_theo_diem_rl(danh_sach):
    return sorted(danh_sach, key=lambda sv: sv.diem_rl)

def tim_sv_diem_tl_cao_nhat(danh_sach):
    return max(danh_sach, key=lambda sv: sv.diem_tl)
