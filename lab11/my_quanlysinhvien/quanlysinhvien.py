import csv
def nhap_danh_sach_sv():
    """
    nhap ds nhan vien tu ban phim
    Trả về danh sách dict mỗi sv gồm: masv, hoten, dtb, drl, dtl
    """
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
    """
    Tinh diem TL = (DTB + DRL)/2
    """
    return (dtb + drl) / 2

def in_danh_sach_sv(ds):
    """
    In danh sach sinh vien ra man hinh theo dang bang
    """
    print(f"{'Ma SV':<10} {'Ho Ten':<25} {'DTB':<8} {'DRL':<8} {'DTL':<8}")
    print('-'*60)
    for sv in ds:
        print(f"{sv['masv']:<10} {sv['hoten']:<25} {sv['dtb']:<8.2f} {sv['drl']:<8.2f} {sv['dtl']:<8.2f}")

def luu_file_csv(filename, ds):
    """
    Luu danh sach sinh vien vao file csv
    """
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['MaSV', 'HoTen', 'DTB', 'DRL', 'DTL'])
        for sv in ds:
            writer.writerow([sv['masv'], sv['hoten'], sv['dtb'], sv['drl'], sv['dtl']])

def sap_xep_theo_drl(ds):
    """
    Sap xep danh sach tang dan theo diem ren luyen (drl)
    """
    return sorted(ds, key=lambda sv: sv['drl'])

def sv_diem_tl_cao_nhat(ds):
    """
    Tim va tra ve sinh vien co diem TL cao nhat
    Neu co nhieu sinh vien diem TL cao bang nhau, tra ve danh sach
    """
    if not ds:
        return []
    max_tl = max(sv['dtl'] for sv in ds)
    return [sv for sv in ds if sv['dtl'] == max_tl]