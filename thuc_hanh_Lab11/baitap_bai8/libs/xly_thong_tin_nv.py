def tinh_luong(he_so):
    return he_so * 1490000

def tinh_phu_cap(chuc_vu):
    if chuc_vu == 'TP':
        return 1000000
    elif chuc_vu == 'PP':
        return 700000
    elif chuc_vu == 'NV':
        return 300000
    else:
        return 0

def tinh_thuc_linh(luong, phu_cap):
    return luong + phu_cap

def hien_thi_danh_sach(ds):
    print("{:<10} {:<20} {:<8} {:<10} {:<12} {:<12} {:<12}".format(
        "Mã NV", "Tên NV", "Chức vụ", "Hệ số", "Lương", "Phụ cấp", "Thực lĩnh"))
    for nv in ds:
        print("{:<10} {:<20} {:<8} {:<10.2f} {:<12,.0f} {:<12,.0f} {:<12,.0f}".format(
            nv['ma_nv'], nv['ten_nv'], nv['chuc_vu'], nv['he_so'],
            nv['luong'], nv['phu_cap'], nv['thuc_linh']))

def sap_xep_theo_thuc_linh(ds):
    return sorted(ds, key=lambda nv: nv['thuc_linh'], reverse=True)

def ghi_file_csv(ds, filename):
    import csv
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Mã NV', 'Tên NV', 'Chức vụ', 'Hệ số', 'Lương', 'Phụ cấp', 'Thực lĩnh'])
        for nv in ds:
            writer.writerow([
                nv['ma_nv'], nv['ten_nv'], nv['chuc_vu'], nv['he_so'],
                nv['luong'], nv['phu_cap'], nv['thuc_linh']
            ])
