import csv
def nhap_danh_sach_sv():
    danh_sach = []
    n = int(input("Nhap so luong sinh vien: "))
    for _ in range(n):
        ma_sv = input("Ma SV: ")
        ho_ten = input("Ho ten SV: ")
        diem_tb = float(input("Diem trung binh: "))
        diem_rl = float(input("Diem ren luyen: "))
        diem_tl = (diem_tb + diem_rl) / 2 
        sv = [ma_sv, ho_ten, diem_tb, diem_rl, diem_tl]
        danh_sach.append(sv)
    return danh_sach
def luu_file_csv(danh_sach, ten_file):
    with open(ten_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Ma SV", "Ho ten SV", "Diem trung binh", "Diem ren luyen", "Diem tich luy"])
        for sv in danh_sach:
            writer.writerow(sv)
def sap_xep_theo_diem_rl(danh_sach):
    return sorted(danh_sach, key=lambda sv: sv[3])
def tim_sv_diem_tl_cao_nhat(danh_sach):
    return max(danh_sach, key=lambda sv: sv[4])