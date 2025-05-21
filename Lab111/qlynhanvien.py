import csv
from libs.xu_ly_thong_tin_nhanvien import *

def nhap_danh_sach_nv():
    danh_sach = []
    n = int(input("Nhập số lượng nhân viên: "))
    for _ in range(n):
        ma = input("Mã NV: ")
        ten = input("Tên NV: ")
        chuc_vu = input("Chức vụ (TP/PP/NV): ")
        hs_luong = float(input("Hệ số lương: "))
        luong = tinh_luong(hs_luong)
        phu_cap = tinh_phu_cap(chuc_vu)
        thuc_linh = tinh_thuc_linh(luong, phu_cap)
        danh_sach.append({
            'MaNV': ma,
            'TenNV': ten,
            'ChucVu': chuc_vu,
            'HeSoLuong': hs_luong,
            'Luong': luong,
            'PhuCap': phu_cap,
            'ThucLinh': thuc_linh
        })
    return danh_sach

def in_danh_sach_nv(danh_sach):
    print(f"{'Mã NV':<10}{'Tên NV':<20}{'Chức vụ':<10}{'HSL':<6}{'Lương':<12}{'PC':<10}{'Thực lĩnh':<12}")
    for nv in danh_sach:
        print(f"{nv['MaNV']:<10}{nv['TenNV']:<20}{nv['ChucVu']:<10}{nv['HeSoLuong']:<6.2f}{nv['Luong']:<12,.0f}{nv['PhuCap']:<10,}{nv['ThucLinh']:<12,.0f}")

def sap_xep_theo_thuc_linh(danh_sach):
    return sorted(danh_sach, key=lambda x: -x['ThucLinh'])

def luu_file_csv(danh_sach, filename='files/ds_nhanvien.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=danh_sach[0].keys())
        writer.writeheader()
        writer.writerows(danh_sach)

def main():
    danh_sach = nhap_danh_sach_nv()
    print("\nDanh sách nhân viên:")
    in_danh_sach_nv(danh_sach)

    print("\nDanh sách sau sắp xếp theo Thực lĩnh giảm dần:")
    danh_sach_sx = sap_xep_theo_thuc_linh(danh_sach)
    in_danh_sach_nv(danh_sach_sx)

    luu_file_csv(danh_sach_sx)
    print("\nDữ liệu đã lưu vào files/ds_nhanvien.csv")

if __name__ == '__main__':
    main()
