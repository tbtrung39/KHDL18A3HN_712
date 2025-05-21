import os
from libs import xly_thong_tin_nv as xl

def nhap_danh_sach_nv():
    ds = []
    n = int(input("Nhập số lượng nhân viên: "))
    for i in range(n):
        print(f"\nNhập thông tin nhân viên thứ {i + 1}:")
        ma_nv = input("Mã NV: ")
        ten_nv = input("Tên NV: ")
        chuc_vu = input("Chức vụ (TP/PP/NV): ")
        he_so = float(input("Hệ số lương: "))
        
        luong = xl.tinh_luong(he_so)
        phu_cap = xl.tinh_phu_cap(chuc_vu)
        thuc_linh = xl.tinh_thuc_linh(luong, phu_cap)

        nv = {
            'ma_nv': ma_nv,
            'ten_nv': ten_nv,
            'chuc_vu': chuc_vu,
            'he_so': he_so,
            'luong': luong,
            'phu_cap': phu_cap,
            'thuc_linh': thuc_linh
        }
        ds.append(nv)
    return ds

def menu():
    danh_sach_nv = []
    while True:
        print("\n--- MENU ---")
        print("1. Nhập danh sách nhân viên")
        print("2. Hiển thị danh sách nhân viên")
        print("3. Hiển thị danh sách giảm dần theo Thực lĩnh")
        print("4. Ghi vào file ds_nhanvien.csv")
        print("0. Thoát")

        chon = input("Chọn chức năng: ")

        if chon == '1':
            danh_sach_nv = nhap_danh_sach_nv()
        elif chon == '2':
            if danh_sach_nv:
                xl.hien_thi_danh_sach(danh_sach_nv)
            else:
                print("Chưa có dữ liệu.")
        elif chon == '3':
            if danh_sach_nv:
                ds_sap_xep = xl.sap_xep_theo_thuc_linh(danh_sach_nv)
                xl.hien_thi_danh_sach(ds_sap_xep)
            else:
                print("Chưa có dữ liệu.")
        elif chon == '4':
            if danh_sach_nv:
                # Tạo thư mục files nếu chưa tồn tại
                os.makedirs('files', exist_ok=True)

                # Ghi vào file đúng đường dẫn
                xl.ghi_file_csv(danh_sach_nv, 'baitap_bai8/files/ds_nhanvien.csv')

                print("Đã ghi file thành công!")
            else:
                print("Chưa có dữ liệu.")
        elif chon == '0':
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    menu()
