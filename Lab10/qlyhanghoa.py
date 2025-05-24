def nhap_du_lieu():
    ds_hang_hoa = []
    n = int(input("Nhap so luong mat hang: "))
    for i in range(n):
        ma_hang = input("Nhap ma hang: ")
        ten_hang = input("Nhap ten hang: ")
        don_vi_tinh = input("Nhap don vi tinh: ")
        don_gia = float(input("Nhap don gia: "))
        so_luong = int(input("Nhap so luong: "))
        thanh_tien = don_gia * so_luong
        thue_vat = thanh_tien * 0.1
        ds_hang_hoa.append({
            "ma_hang": ma_hang,
            "ten_hang": ten_hang,
            "don_vi_tinh": don_vi_tinh,
            "don_gia": don_gia,
            "so_luong": so_luong,
            "thanh_tien": thanh_tien,
            "thue_vat": thue_vat
        })
    return ds_hang_hoa
def thong_tin(ds):
    for hang in ds:
        print(hang)
def sap_xep_theo_thue(ds):
    return sorted(ds, key=lambda x: x["thue_vat"], reverse=True)