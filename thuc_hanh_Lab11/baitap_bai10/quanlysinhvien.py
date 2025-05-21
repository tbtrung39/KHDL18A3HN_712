import csv

def tinh_tich_luy(tb, rl):
    return (tb + rl) / 2

def hien_thi_danh_sach(ds):
    print(f"{'Mã SV':<10}{'Họ tên':<20}{'TB':<10}{'RL':<10}{'TL':<10}")
    for sv in ds:
        print(f"{sv['ma_sv']:<10}{sv['ho_ten']:<20}{sv['tb']:<10}{sv['rl']:<10}{sv['tl']:<10}")

def sap_xep_theo_rl(ds):
    return sorted(ds, key=lambda x: x['rl'])

def tim_sv_tl_max(ds):
    max_tl = max(sv['tl'] for sv in ds)
    return [sv for sv in ds if sv['tl'] == max_tl]

def ghi_file_csv(ds, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Mã SV', 'Họ tên', 'TB', 'RL', 'TL'])
        for sv in ds:
            writer.writerow([sv['ma_sv'], sv['ho_ten'], sv['tb'], sv['rl'], sv['tl']])
