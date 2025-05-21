from My_QuanLySinhVien import quanlysinhvien as qlsv

def main():
    ds_sv = qlsv.nhap_danh_sach_sv()

    print("\nDanh sach sinh vien vua nhap:")
    qlsv.in_danh_sach_sv(ds_sv)

    # Luu
    qlsv.luu_file_csv('files/ds_sinhvien.csv', ds_sv)
    print("\nDa luu danh sach sinh vien vao file files/ds_sinhvien.csv")
    ds_sv_sap_xep = qlsv.sap_xep_theo_drl(ds_sv)
    print("\nDanh sach sinh vien sau khi sap xep theo diem ren luyen tang dan:")
    qlsv.in_danh_sach_sv(ds_sv_sap_xep)

    sv_max_tl = qlsv.sv_diem_tl_cao_nhat(ds_sv)
    print("\nSinh vien co diem TL cao nhat:")
    qlsv.in_danh_sach_sv(sv_max_tl)

if __name__ == "__main__":
    main()
