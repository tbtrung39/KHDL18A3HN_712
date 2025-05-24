import csv
from libs import xu_ly_thong_tin_nhanvien as xl

ds_nhan_vien = []

def nhap_ds_nhan_vien():
    while True:
        ma = input("Mã NV: ")
        ten = input("Tên NV: ")
        chuc_vu = input("Chức vụ (TP/PP/NV): ")
        he_so = float(input("Hệ số lương: "))

        luong = xl.tinh_luong(he_so)
        phu_cap = xl.tinh_phu_cap_chuc_vu(chuc_vu)
        thuc_linh = xl.tinh_thuc_linh(luong, phu_cap)


        ds_nhan_vien.append([ma, ten, chuc_vu, he_so, luong, phu_cap, thuc_linh])

        tiep = input("Nhập thêm? (c/k): ")
        if tiep.lower() != 'c':
            break

def hien_thi_danh_sach():
    print("{:<10} {:<20} {:<8} {:<10} {:<10} {:<10} {:<10}".format(
        "Ma NV", "Ten NV", "Chuc vu", "He so", "Luong", "Phu cap", "Thuc linh"))
    for nv in ds_nhan_vien:
        print("{:<10} {:<20} {:<8} {:<10} {:<10,.0f} {:<10,.0f} {:<10,.0f}".format(*nv))

def sap_xep_theo_thuc_linh():
    ds = sorted(ds_nhan_vien, key=lambda x: x[-1], reverse=True)
    print("Danh sách sắp xếp theo Thực lĩnh:")
    for nv in ds:
        print("{:<10} {:<20} {:<8} {:<10} {:<10,.0f} {:<10,.0f} {:<10,.0f}".format(*nv))

def luu_file():
    with open(r"lab_11\bai_08\LAB11\files\ds_nhanvien.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["MaNV", "TenNV", "ChucVu", "HeSo", "Luong", "PhuCap", "ThucLinh"])
        writer.writerows(ds_nhan_vien)
    print("Đã lưu vào files/ds_nhanvien.csv")

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Nhập danh sách nhân viên")
        print("2. Hiển thị danh sách")
        print("3. Sắp xếp theo Thực lĩnh")
        print("4. Lưu file")
        print("0. Thoát")
        chon = input("Chọn: ")

        if chon == "1":
            nhap_ds_nhan_vien()
        elif chon == "2":
            hien_thi_danh_sach()
        elif chon == "3":
            sap_xep_theo_thuc_linh()
        elif chon == "4":
            luu_file()
        elif chon == "0":
            break
        else:
            print("Chọn sai!")

if __name__ == "__main__":
    menu()