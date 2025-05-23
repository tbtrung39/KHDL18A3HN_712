from libs.xu_ly_thong_tin_nhanvien import nhap_nhan_vien, tinh_luong, in_danh_sach, sap_xep_thuc_linh, luu_file

def main():
    ds_nv = nhap_nhan_vien()
    tinh_luong(ds_nv)
    in_danh_sach(ds_nv, "Danh sách nhân viên trước khi sắp xếp")
    
    sap_xep_thuc_linh(ds_nv)
    in_danh_sach(ds_nv, "Danh sách nhân viên sau khi sắp xếp theo Thực lĩnh giảm dần")
    
    file_luu = "D:/Toan/Python uneti/THLT HK2/lab_11/Cau_08/LAB11/files/ds_nhanvien.csv"
    luu_file(ds_nv, file_luu)
    print(f"\nDữ liệu đã được lưu vào file {file_luu}")

if __name__ == "__main__":
    main()
