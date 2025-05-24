import csv
def nhap_danh_sach():
    ds_sinhvien = []
    print("Nhập thông tin sinh viên (nhấn Enter để dừng):")
    while True:
        ma_sv = input("Mã sinh viên: ").strip()
        if not ma_sv:
            break
        ho_ten = input("Họ và tên: ").strip()
        diem_tb = float(input("Điểm trung bình: ").strip())
        diem_rl = float(input("Điểm rèn luyện: ").strip())
        ds_sinhvien.append({
            "ma_sv": ma_sv,
            "ho_ten": ho_ten,
            "diem_tb": diem_tb,
            "diem_rl": diem_rl
        })
    return ds_sinhvien

def tinh_diem_tl(ds_sinhvien):
    for sv in ds_sinhvien:
        sv["diem_tl"] = (sv["diem_tb"] + sv["diem_rl"]) / 2

def in_danh_sach(ds_sinhvien):
    print(f"{'Mã SV':<10}{'Họ và tên':<20}{'Điểm TB':<10}{'Điểm RL':<10}{'Điểm TL':<10}")
    print("-" * 60)
    for sv in ds_sinhvien:
        print(f"{sv['ma_sv']:<10}{sv['ho_ten']:<20}{sv['diem_tb']:<10.2f}{sv['diem_rl']:<10.2f}{sv['diem_tl']:<10.2f}")

def luu_file(ds_sinhvien):
    duong_dan = input("Nhập đường dẫn file để lưu (ví dụ: files/ds_sinhvien.csv): ").strip()
    with open(duong_dan, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["ma_sv", "ho_ten", "diem_tb", "diem_rl", "diem_tl"])
        writer.writeheader()
        writer.writerows(ds_sinhvien)
    print(f"Danh sách đã được lưu vào file '{duong_dan}'.")

def sap_xep(ds_sinhvien):
    return sorted(ds_sinhvien, key=lambda sv: sv["diem_rl"])

def in_sv_diem_tl_cao_nhat(ds_sinhvien):
    if not ds_sinhvien:
        print("Danh sách sinh viên trống!")
        return
    sv_max = max(ds_sinhvien, key=lambda sv: sv["diem_tl"])
    print("Thông tin sinh viên có điểm TL cao nhất:")
    print(f"Mã SV: {sv_max['ma_sv']}, Họ và tên: {sv_max['ho_ten']}, Điểm TL: {sv_max['diem_tl']:.2f}")
