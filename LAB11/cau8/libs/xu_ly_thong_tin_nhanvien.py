def nhap_danh_sach():
    ds = []
    while True:
        ma_nv = input("Nhập mã nhân viên (bỏ trống để dừng): ").strip()
        if not ma_nv:
            break
        ten_nv = input("Nhập tên nhân viên: ").strip()
        chuc_vu = input("Nhập chức vụ (TP/PP/NV): ").strip().upper()
        hsl = float(input("Nhập hệ số lương: "))
        ds.append({
            "ma_nv": ma_nv,
            "ten_nv": ten_nv,
            "chuc_vu": chuc_vu,
            "hsl": hsl,
            "luong": 0,
            "phu_cap": 0,
            "thuc_linh": 0
        })
    return ds

def tinh_toan_thong_tin(ds):
    """Tính toán Lương, Phụ cấp, Thực lĩnh cho danh sách nhân viên."""
    for nv in ds:
        nv['luong'] = float(nv['hsl']) * 1490000
        if nv['chuc_vu'] == 'TP':
            nv['phu_cap'] = 1000000
        elif nv['chuc_vu'] == 'PP':
            nv['phu_cap'] = 700000
        elif nv['chuc_vu'] == 'NV':
            nv['phu_cap'] = 300000
        else:
            nv['phu_cap'] = 0
        nv['thuc_linh'] = nv['luong'] + nv['phu_cap']

def in_bang(ds):
    """In danh sách nhân viên dưới dạng bảng."""
    if not ds:
        print("Danh sách rỗng.")
        return
    print(f"{'Mã NV':<10}{'Tên NV':<20}{'Chức vụ':<10}{'HSL':<9}{'Lương':<10}{'Phụ cấp':<10}{'Thực lĩnh':<10}")
    print("-" * 75)
    for nv in ds:
        print(f"{nv['ma_nv']:<10}{nv['ten_nv']:<20}{nv['chuc_vu']:<10}{float(nv['hsl']):<9.2f}{nv['luong']:<10.0f}{nv['phu_cap']:<10.0f}{nv['thuc_linh']:<10.0f}")

def sap_xep(ds):
    return sorted(ds, key=lambda x: x["thuc_linh"], reverse=True)