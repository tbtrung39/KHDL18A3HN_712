from My_QuanLySinhvien import quanlysinhvien
def main():
    print("------CHUONG TRINH QUAN LY SINH VIEN------")
    danh_sach = quanlysinhvien.nhap_danh_sach_sv()
    ten_file = "Bai10/files/ds_sinhvien.csv"
    quanlysinhvien.luu_file_csv(danh_sach, ten_file)
    print("Da luu danh sach vao file:",ten_file)
    print("Danh sach sau khi sap xep diem ren luyen theo tang dan:")
    danh_sach_sap_xep = quanlysinhvien.sap_xep_theo_diem_rl(danh_sach)
    for sv in danh_sach_sap_xep:
        print(f"{sv[0]} - {sv[1]} | TB: {sv[2]} | RL: {sv[3]} | TL: {sv[4]}")
    sv_max = quanlysinhvien.tim_sv_diem_tl_cao_nhat(danh_sach)
    print("Sinh vien co diem tich luy cao nhat:")
    print(f"{sv_max[0]} - {sv_max[1]} | TB: {sv_max[2]} | RL: {sv_max[3]} | TL: {sv_max[4]}")
if __name__ == "__main__":
    main()