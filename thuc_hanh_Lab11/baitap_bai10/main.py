from quanlysinhvien import *
import os

def nhap_danh_sach_sv():
    ds = []
    n = int(input("Nhập số lượng sinh viên: "))
    for i in range(n):
        print(f"\nNhập sinh viên thứ {i + 1}:")
        ma_sv = input("Mã SV: ")
        ho_ten = input("Họ tên: ")
        tb = float(input("Điểm TB: "))
        rl = float(input("Điểm RL: "))
        tl = tinh_tich_luy(tb, rl)
        sv = {
            'ma_sv': ma_sv,
            'ho_ten': ho_ten,
            'tb': tb,
            'rl': rl,
            'tl': tl
        }
        ds.append(sv)
    return ds

def menu():
    ds_sv = []
    while True:
        print("\n--- MENU ---")
        print("1. Nhập danh sách sinh viên")
        print("2. Hiển thị danh sách")
        print("3. Sắp xếp theo RL tăng dần")
        print("4. Hiển thị SV có TL cao nhất")
        print("5. Ghi file ds_sinhvien.csv")
        print("0. Thoát")

        chon = input("Chọn chức năng: ")
        if chon == '1':
            ds_sv = nhap_danh_sach_sv()
        elif chon == '2':
            hien_thi_danh_sach(ds_sv)
        elif chon == '3':
            ds_sap_xep = sap_xep_theo_rl(ds_sv)
            hien_thi_danh_sach(ds_sap_xep)
        elif chon == '4':
            ds_max = tim_sv_tl_max(ds_sv)
            print("\nSinh viên có TL cao nhất:")
            hien_thi_danh_sach(ds_max)
        elif chon == '5':
            os.makedirs('files', exist_ok=True)
            ghi_file_csv(ds_sv, 'files/ds_sinhvien.csv')
            print("Đã ghi file thành công!")
        elif chon == '0':
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    menu()
