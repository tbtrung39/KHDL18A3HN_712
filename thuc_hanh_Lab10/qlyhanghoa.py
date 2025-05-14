def nhap_danh_sach_mat_hang():
    danh_sach = []
    n = int(input("Nhập số lượng mặt hàng: "))
    for i in range(n):
        print(f"\nNhập thông tin mặt hàng thứ {i+1}:")
        ma = input("Mã hàng (4 ký tự): ")
        ten = input("Tên hàng: ")
        dvt = input("Đơn vị tính: ")
        dg = float(input("Đơn giá: "))
        sl = int(input("Số lượng: "))
        thanh_tien = dg * sl
        thue = thanh_tien * 0.10
        mat_hang = {
            'ma': ma,
            'ten': ten,
            'dvt': dvt,
            'dongia': dg,
            'soluong': sl,
            'thanhtien': thanh_tien,
            'thue': thue
        }
        danh_sach.append(mat_hang)
    return danh_sach

def in_danh_sach(danh_sach):
    print(f"\n{'Mã':<6} {'Tên hàng':<20} {'ĐVT':<10} {'Đơn giá':<10} {'SL':<5} {'Thành tiền':<15} {'Thuế':<10}")
    for mh in danh_sach:
        print(f"{mh['ma']:<6} {mh['ten']:<20} {mh['dvt']:<10} {mh['dongia']:<10.2f} {mh['soluong']:<5} {mh['thanhtien']:<15.2f} {mh['thue']:<10.2f}")

def sap_xep_theo_thue_giam_dan(danh_sach):
    return sorted(danh_sach, key=lambda mh: mh['thue'], reverse=True)
