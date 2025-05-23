import csv

def tinh_luong(he_so):
    return he_so * 1490000

def tinh_phu_cap(chuc_vu):
    return 1000000 if chuc_vu == "TP" else 700000 if chuc_vu == "PP" else 300000

def main():
    ds = []
    while True:
        ma = input("Mã NV: ")
        if not ma: break
        ten = input("Tên NV: ")
        cv = input("Chức vụ: ")
        hs = float(input("Hệ số lương: "))
        luong = tinh_luong(hs)
        pc = tinh_phu_cap(cv)
        tl = luong + pc
        ds.append([ma, ten, cv, hs, luong, pc, tl])

    ds.sort(key=lambda x: -x[6])

    with open("files/ds_nhanvien.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Mã", "Tên", "Chức vụ", "HS", "Lương", "PC", "Thực lĩnh"])
        writer.writerows(ds)

if __name__ == "__main__":
    main()
