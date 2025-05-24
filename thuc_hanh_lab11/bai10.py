import csv
def tinh_diem_tich_luy(tb, rl):
    return round((tb + rl) / 2, 2)
def nhap_danh_sach_sv():
    ds = []
    n = int(input("Nhập số sinh viên: "))
    for _ in range(n):
        masv = input("Mã SV: ")
        hoten = input("Họ tên: ")
        diem_tb = float(input("Điểm TB: "))
        diem_rl = float(input("Điểm RL: "))
        diem_tl = tinh_diem_tich_luy(diem_tb, diem_rl)
        ds.append({
            'MaSV': masv,
            'HoTen': hoten,
            'DiemTB': diem_tb,
            'DiemRL': diem_rl,
            'DiemTL': diem_tl
        })
    return ds
def in_bang_sv(ds):
    print(f"{'Mã SV':<10}{'Họ tên':<20}{'TB':<6}{'RL':<6}{'TL':<6}")
    for sv in ds:
        print(f"{sv['MaSV']:<10}{sv['HoTen']:<20}{sv['DiemTB']:<6.2f}{sv['DiemRL']:<6.2f}{sv['DiemTL']:<6.2f}")
def luu_file_csv(ds, filename='files/ds_sinhvien.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=ds[0].keys())
        writer.writeheader()
        writer.writerows(ds)
def sap_xep_theo_diem_rl(ds):
    return sorted(ds, key=lambda sv: sv['DiemRL'])
def sinhvien_diem_tl_max(ds):
    max_tl = max(ds, key=lambda sv: sv['DiemTL'])
    return [sv for sv in ds if sv['DiemTL'] == max_tl['DiemTL']]