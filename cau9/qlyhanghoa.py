def nhap_danh_sach_mat_hang():
    ds = []
    so_mat_hang = int(input("Nhap so luong mat hang: "))
    for i in range(so_mat_hang):
        print(f"\nNhap thong tin mat hang thu {i+1}:")
        ma = input("  Ma hang (4 ky tu): ")
        ten = input("  Ten hang: ")
        dvt = input("  Don vi tinh: ")
        dongia = float(input("  Don gia: "))
        soluong = int(input("  So luong: "))
        thanhtien = dongia * soluong
        thue = thanhtien * 0.10
        ds.append({
            "ma": ma,
            "ten": ten,
            "dvt": dvt,
            "dongia": dongia,
            "soluong": soluong,
            "thanhtien": thanhtien,
            "thue": thue
        })
    return ds
def hien_thi_danh_sach(ds):
    print("\n{:<10} {:<15} {:<10} {:<10} {:<10} {:<12} {:<10}".format(
        "Ma hang", "Ten hang", "DVT", "Don gia", "So luong", "Thanh tien", "Thue"))
    for mh in ds:
        print("{:<10} {:<15} {:<10} {:<10.2f} {:<10} {:<12.2f} {:<10.2f}".format(
            mh["ma"], mh["ten"], mh["dvt"], mh["dongia"],
            mh["soluong"], mh["thanhtien"], mh["thue"]
        ))
def sap_xep_theo_thue(ds):
    return sorted(ds, key=lambda mh: mh["thue"], reverse=True)
