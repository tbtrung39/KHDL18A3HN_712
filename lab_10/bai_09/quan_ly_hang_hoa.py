def nhap_danh_sach_hang(n):
    ds = []
    for i in range(n):
        print(f"\nNhap thong tin mat hang thu {i+1}:")
        ma = input("Ma hang(4 ky tu): ")
        ten = input("Ten hang: ")
        dvt = input("Don vi tinh: ")
        dongia = float(input("Don gia: "))
        soluong = int(input("So luong: "))
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
    print(f"{'Ma':<6}{'Ten hang':<15}{'DVT':<10}{'Don gia':<10}{'SL':<8}{'Thanh tien':<15}{'Thue':<10}")
    for hang in ds:
        print(f"{hang['ma']:<6}{hang['ten']:<15}{hang['dvt']:<10}{hang['dongia']:<10.2f}"
              f"{hang['soluong']:<8}{hang['thanhtien']:<15.2f}{hang['thue']:<10.2f}")

def sap_xep_theo_thue(ds):
    return sorted(ds, key=lambda h: h["thue"], reverse=True)