import csv
import os
LUONG_CO_BAN = 1490000
PHU_CAP = {
    'TP': 1000000,
    'PP': 700000,
    'NV': 300000
}
danh_sach_nv = []
def nhap_nhan_vien():
    print("Nhap thong tin nhan vien (nhap rong o Ma nhan vien de ket thuc):")
    while True:
        ma_nv = input("Ma nhan vien: ").strip()
        if ma_nv == '':
            break
        ho_ten = input("Ho ten: ").strip()
        he_so_luong = float(input("He so luong: "))
        chuc_vu = input("Chuc vu (TP/PP/NV): ").strip().upper()
        if chuc_vu not in PHU_CAP:
            print("Chuc vu khong hop le, mac dinh la NV")
            chuc_vu = 'NV'
        nv = {
            'MaNV': ma_nv,
            'HoTen': ho_ten,
            'HeSoLuong': he_so_luong,
            'ChucVu': chuc_vu
        }
        danh_sach_nv.append(nv)
    print("Nhap danh sach nhan vien hoan tat.\n")
def tinh_luong_va_phucap():
    for nv in danh_sach_nv:
        luong = nv['HeSoLuong'] * LUONG_CO_BAN
        phu_cap = PHU_CAP.get(nv['ChucVu'], 0)
        thuc_linh = luong + phu_cap
        nv['Luong'] = luong
        nv['PhuCap'] = phu_cap
        nv['ThucLinh'] = thuc_linh
def in_danh_sach(danh_sach):
    if not danh_sach:
        print("Danh sach nhan vien trong.")
        return
    print(f"{'Ma NV':<10} {'Ho Ten':<25} {'HS Luong':<10} {'Chuc vu':<8} {'Luong':<12} {'Phu cap':<10} {'Thuc linh':<12}")
    print("-" * 90)
    for nv in danh_sach:
        print(f"{nv['MaNV']:<10} {nv['HoTen']:<25} {nv['HeSoLuong']:<10.2f} {nv['ChucVu']:<8} {nv['Luong']:<12,.0f} {nv['PhuCap']:<10,} {nv['ThucLinh']:<12,.0f}")
def sap_xep_va_in():
    danh_sach_sap_xep = sorted(danh_sach_nv, key=lambda x: x['ThucLinh'], reverse=True)
    print("\nDanh sach nhan vien sau khi sap xep theo Thuc linh giam dan:")
    in_danh_sach(danh_sach_sap_xep)
def luu_vao_file():
    thu_muc = 'files'
    if not os.path.exists(thu_muc):
        os.mkdir(thu_muc)
    duong_dan = os.path.join(thu_muc, 'ds_nhanvien.csv')
    with open(duong_dan, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['MaNV', 'HoTen', 'HeSoLuong', 'ChucVu', 'Luong', 'PhuCap', 'ThucLinh'])
        for nv in danh_sach_nv:
            writer.writerow([
                nv['MaNV'],
                nv['HoTen'],
                f"{nv['HeSoLuong']:.2f}",
                nv['ChucVu'],
                f"{nv['Luong']:.0f}",
                f"{nv['PhuCap']}",
                f"{nv['ThucLinh']:.0f}"
            ])
            print(f"Du lieu da duoc luu vao file {duong_dan}")
def menu():
    while True:
        print("\n----- QUAN LY NHAN VIEN -----")
        print("1. Nhap danh sach nhan vien")
        print("2. Tinh luong, phu cap va thuc linh")
        print("3. In danh sach nhan vien")
        print("4. Sap xep va in danh sach nhan vien theo thuc linh giam dan")
        print("5. Luu du lieu vao file ds_nhanvien.csv")
        print("0. Thoat chuong trinh")
        chon = input("Chon chuc nang: ")
        if chon == '1':
            nhap_nhan_vien()
        elif chon == '2':
            if not danh_sach_nv:
                print("Chua co du lieu nhan vien, vui long nhap truoc.")
            else:
                tinh_luong_va_phucap()
                print("Da tinh xong luong, phu cap va thuc linh.")
        elif chon == '3':
            in_danh_sach(danh_sach_nv)
        elif chon == '4':
            if not danh_sach_nv or 'ThucLinh' not in danh_sach_nv[0]:
                print("Ban can tinh luong truoc khi sap xep.")
            else:
                sap_xep_va_in()
        elif chon == '5':
            if not danh_sach_nv or 'ThucLinh' not in danh_sach_nv[0]:
                print("Ban can tinh luong truoc khi luu file.")
            else:
                luu_vao_file()
        elif chon == '0':
            print("Thoat chuong trinh. Tam biet!")
            break
        else:
            print("Lua chon khong hop le, vui long chon lai.")
if __name__ == "__main__":
    menu()