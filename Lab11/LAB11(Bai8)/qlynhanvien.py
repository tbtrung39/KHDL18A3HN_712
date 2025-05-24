import csv
from libs.xu_ly_thong_tin_nhanvien import tinh_luong, tinh_phu_cap, tinh_thuc_linh
def nhap_nhan_vien():
    danh_sach = []
    so_nv = int(input("Nhap so luong nhan vien: "))
    for i in range(so_nv):
        ma = input("Ma NV: ")
        ten = input("Ten NV: ")
        chuc_vu = input("Chuc vu (TP/PP/NV): ")
        he_so = float(input("He so luong: "))
        luong = tinh_luong(he_so)
        phu_cap = tinh_phu_cap(chuc_vu)
        thuc_linh = tinh_thuc_linh(he_so, chuc_vu)
        danh_sach.append([ma, ten, chuc_vu, he_so, luong, phu_cap, thuc_linh])
    return danh_sach
def hien_thi(danh_sach):
    print(f"{'Ma':<10}{'Ten':<20}{'Chuc vu':<10}{'He so luong':<5}{'Luong':<12}{'Phu cap':<10}{'Thuc linh':<12}")
    for nv in danh_sach:
        print(f"{nv[0]:<10}{nv[1]:<20}{nv[2]:<10}{nv[3]:<5.2f}{nv[4]:<12,.0f}{nv[5]:<10,.0f}{nv[6]:<12,.0f}")
def sap_xep_giam_theo_thuc_linh(danh_sach):
    return sorted(danh_sach, key=lambda nv: nv[6], reverse=True)
def luu_file(danh_sach, filename="LAB11(Bai8)/files/ds_nhanvien.csv"):
    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Ma", "Ten", "Chuc vu", "He so", "Luong", "Phu cap", "Thuc linh"])
        writer.writerows(danh_sach)
    print("Đã lưu vào file",filename)
def menu():
    danh_sach_nv = []
    while True:
        print("--- MENU ---")
        print("1. Nhap danh sach nhan vien")
        print("2. Hien thi danh sach nhan vien")
        print("3. Sap xep giam dan theo thuc linh va hien thi thong tin")
        print("4. Luu vao file ds_nhanvien.csv")
        print("0. Thoat")
        chon = input("Chon: ")     
        if chon == "1":
            danh_sach_nv = nhap_nhan_vien()
        elif chon == "2":
            hien_thi(danh_sach_nv)
        elif chon == "3":
            danh_sach_nv = sap_xep_giam_theo_thuc_linh(danh_sach_nv)
            hien_thi(danh_sach_nv)
        elif chon == "4":
            luu_file(danh_sach_nv)
        elif chon == "0":
            break
        else:
            print("Khong hop le!")
if __name__=="__main__":
    menu()