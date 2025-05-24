import csv

def nhap_danh_sach_sv():
    ds = []
    n = int(input("Nhap so luong sinh vien: "))
    for i in range(n):
        print(f"\nNhap thong tin sinh vien thu {i+1}:")
        masv = input("Ma sinh vien: ")
        hoten = input("Ho ten: ")
        dtb = float(input("Diem trung binh: "))
        drl = float(input("Diem ren luyen: "))
        dtl = tinh_diem_tl(dtb, drl)
        sv = {
            'masv': masv,
            'hoten': hoten,
            'dtb': dtb,
            'drl': drl,
            'dtl': dtl
        }
        ds.append(sv)
    return ds

def tinh_diem_tl(dtb, drl):
    return (dtb + drl) / 2

def in_danh_sach_sv(ds):
    print(f"{'Ma SV':<10} {'Ho Ten':<25} {'DTB':<8} {'DRL':<8} {'DTL':<8}")
    print('-'*60)
    for sv in ds:
        print(f"{sv['masv']:<10} {sv['hoten']:<25} {sv['dtb']:<8.2f} {sv['drl']:<8.2f} {sv['dtl']:<8.2f}")

def luu_file_csv(filename, ds):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['MaSV', 'HoTen', 'DTB', 'DRL', 'DTL'])
        for sv in ds:
            writer.writerow([sv['masv'], sv['hoten'], sv['dtb'], sv['drl'], sv['dtl']])

def sap_xep_theo_drl(ds):
    return sorted(ds, key=lambda sv: sv['drl'])

def sv_diem_tl_cao_nhat(ds):
    if not ds:
        return []
    max_tl = max(sv['dtl'] for sv in ds)
    return [sv for sv in ds if sv['dtl'] == max_tl]