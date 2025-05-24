from My_QuanLySinhvien.quanlysinhvien import (
    nhap_danh_sach,
    tinh_diem_tl,
    in_danh_sach,
    luu_file,
    sap_xep,
    in_sv_diem_tl_cao_nhat
)

def main():
    ds_sinhvien = nhap_danh_sach()
    if not ds_sinhvien:
        print("Danh sách sinh viên trống. Thoát chương trình.")
        return
    
    tinh_diem_tl(ds_sinhvien)
    
    print("\nDanh sách sinh viên đầy đủ thông tin:")
    in_danh_sach(ds_sinhvien)
    
    print("\nLưu danh sách vào file:")
    luu_file(ds_sinhvien)
    
    print("\nDanh sách sinh viên sắp xếp theo điểm RL tăng dần:")
    ds_sinhvien = sap_xep(ds_sinhvien)
    in_danh_sach(ds_sinhvien)
    
    print("\nSinh viên có điểm TL cao nhất:")
    in_sv_diem_tl_cao_nhat(ds_sinhvien)

if __name__ == "__main__":
    main()
