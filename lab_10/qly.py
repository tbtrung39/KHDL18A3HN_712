def nhap_mat_hang():
    danh_sach = []
    n = int(input("Nhập số lượng mặt hàng: "))
    for i in range(n):
        print(f"\n--- Nhập thông tin mặt hàng thứ {i+1} ---")
        ma_hang = input("Mã hàng (4 ký tự): ").strip()[:4]
        ten_hang = input("Tên hàng: ")
        don_vi_tinh = input("Đơn vị tính: ")
        don_gia = float(input("Đơn giá: "))
        so_luong = int(input("Số lượng: "))

        mat_hang = {
            "ma_hang": ma_hang,
            "ten_hang": ten_hang,
            "don_vi_tinh": don_vi_tinh,
            "don_gia": don_gia,
            "so_luong": so_luong,
            "thanh_tien": 0,
            "thue": 0 
        }
        danh_sach.append(mat_hang)
    return danh_sach

def tinh_thanh_tien_va_thue(danh_sach):
    for hang in danh_sach:
        hang["thanh_tien"] = hang["don_gia"] * hang["so_luong"]
        hang["thue"] = hang["thanh_tien"] * 0.1

def in_danh_sach(danh_sach):
    print(f"\n{'Mã hàng':<8} {'Tên hàng':<20} {'ĐVT':<10} {'Đơn giá':<10} {'SL':<5} {'Thành tiền':<15} {'Thuế (10%)':<12}")
    print("-" * 85)
    for hang in danh_sach:
        print(f"{hang['ma_hang']:<8} {hang['ten_hang']:<20} {hang['don_vi_tinh']:<10} "
              f"{hang['don_gia']:<10.2f} {hang['so_luong']:<5} "
              f"{hang['thanh_tien']:<15.2f} {hang['thue']:<12.2f}")

def sap_xep_giam_theo_thue(danh_sach):
    return sorted(danh_sach, key=lambda x: x["thue"], reverse=True)
