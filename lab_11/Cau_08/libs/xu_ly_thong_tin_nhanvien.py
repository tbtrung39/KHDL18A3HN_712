import csv

PHU_CAP = {
    "TP": 1_000_000,
    "PP": 700_000,
    "NV": 300_000
}
def nhap_nhan_vien():
    ds_nv = []
    n = int(input("Nhập số lượng nhân viên: "))
    for i in range(n):
        print(f"Nhập thông tin nhân viên thứ {i+1}:")
        ma_nv = input("  Mã NV: ").strip()
        ho_ten = input("  Họ tên: ").strip()
        he_so_luong = float(input("  Hệ số lương: "))
        chuc_vu = input("  Chức vụ (TP/PP/NV): ").strip().upper()
        ds_nv.append({
            "ma_nv": ma_nv,
            "ho_ten": ho_ten,
            "he_so_luong": he_so_luong,
            "chuc_vu": chuc_vu
        })
    return ds_nv

def tinh_luong(ds_nv):
    for nv in ds_nv:
        luong = nv["he_so_luong"] * 1490000
        phu_cap = PHU_CAP.get(nv["chuc_vu"], 0)
        thuc_linh = luong + phu_cap
        nv["luong"] = luong
        nv["phu_cap"] = phu_cap
        nv["thuc_linh"] = thuc_linh

def in_danh_sach(ds_nv, title="Danh sách nhân viên"):
    print(f"\n{title}:")
    print(f"{'Mã NV':<10} {'Họ tên':<20} {'Hệ số Lương':<12} {'Chức vụ':<6} {'Lương':<12} {'Phụ cấp':<10} {'Thực lĩnh':<12}")
    print("-"*90)
    for nv in ds_nv:
        print(f"{nv['ma_nv']:<10} {nv['ho_ten']:<20} {nv['he_so_luong']:<12.2f} {nv['chuc_vu']:<6} {nv['luong']:<12,.0f} {nv['phu_cap']:<10,.0f} {nv['thuc_linh']:<12,.0f}")

def sap_xep_thuc_linh(ds_nv):
    ds_nv.sort(key=lambda x: x["thuc_linh"], reverse=True)

def luu_file(ds_nv, file_path):
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Mã NV", "Họ tên", "Hệ số lương", "Chức vụ", "Lương", "Phụ cấp", "Thực lĩnh"])
        for nv in ds_nv:
            writer.writerow([
                nv["ma_nv"], nv["ho_ten"], nv["he_so_luong"], nv["chuc_vu"],
                f"{nv['luong']:.0f}", f"{nv['phu_cap']:.0f}", f"{nv['thuc_linh']:.0f}"
            ])
