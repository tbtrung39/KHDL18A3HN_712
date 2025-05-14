def nhap_danh_sach_hang(n):
    ds = []
    for i in range(n):
        print(f"\nNhập thông tin mặt hàng thứ {i+1}:")
        ma = input("Mã hàng (4 ký tự): ")
        ten = input("Tên hàng: ")
        dvt = input("Đơn vị tính: ")
        dongia = float(input("Đơn giá: "))
        soluong = int(input("Số lượng: "))
        thanhtien = dongia * soluong
        thue = thanhtien * 0.1
        hang = {
            "ma": ma,
            "ten": ten,
            "dvt": dvt,
            "dongia": dongia,
            "soluong": soluong,
            "thanhtien": thanhtien,
            "thue": thue
        }
        ds.append(hang)
    return ds

def hien_thi_danh_sach(ds):
    print(f"{'Mã':<6}{'Tên hàng':<15}{'ĐVT':<10}{'Đơn giá':<10}{'SL':<8}{'Thành tiền':<15}{'Thuế':<10}")
    for hang in ds:
        print(f"{hang['ma']:<6}{hang['ten']:<15}{hang['dvt']:<10}{hang['dongia']:<10.2f}"
              f"{hang['soluong']:<8}{hang['thanhtien']:<15.2f}{hang['thue']:<10.2f}")

def sap_xep_theo_thue(ds):
    return sorted(ds, key=lambda h: h["thue"], reverse=True)
